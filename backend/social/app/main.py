from os import environ
from models import DB_URL, UserProfile, TenantProfile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, jsonify

from fastapi import FastAPI

app = FastAPI()

engine = create_engine(DB_URL)

# Create a session class
Session = sessionmaker(bind=engine

@app.get("/")
def read_root():
    return {"message": f"App is running on port. {environ.get('SOCIAL_PORT')}"}

@app.route('/api/user_profiles', methods=['POST'])
def create_user_profile():
    session = Session()
    data = request.json
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    department = data.get('department')
    designation = data.get('designation')
    tenant_id = data.get('tenant_id')
    image_url = data.get('image_url')
    city = data.get('city')
    country = data.get('country')
    bio = data.get('bio')
    social_links = data.get('social_links')
    employee_id = data.get('employee_id')

    # Create a new UserProfile instance with extracted data
    user_profile = UserProfile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        department=department,
        designation=designation,
        tenant_id=tenant_id,
        image_url=image_url,
        city=city,
        country=country,
        bio=bio,
        social_links=social_links,
        employee_id=employee_id
    )

    session.add(user_profile)
    session.commit()
    session.close()
    return jsonify(message='User profile created successfully'), 201

@app.route('/api/user_profiles', methods=['GET'])
def get_all_user_profiles():
    session = Session()
    user_profiles = session.query(UserProfile).all()
    session.close()
    return jsonify(user_profiles=[profile.serialize() for profile in user_profiles])

@app.route('/api/user_profiles/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    session = Session()
    user_profile = session.query(UserProfile).get(user_id)
    session.close()
    if user_profile:
        return jsonify(user_profile.serialize())
    else:
        return jsonify(message='User profile not found'), 404

@app.route('/api/user_profiles/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    session = Session()
    user_profile = session.query(UserProfile).get(user_id)
    if user_profile:
        session.delete(user_profile)
        session.commit()
        session.close()
        return jsonify(message='User profile deleted successfully')
    else:
        session.close()
        return jsonify(message='User profile not found'), 404

@app.route('/api/user_profiles/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    session = Session()
    user_profile = session.query(UserProfile).get(user_id)
    if user_profile:
        data = request.json
        for key, value in data.items():
            setattr(user_profile, key, value)
        session.commit()
        session.close()
        return jsonify(message='User profile updated successfully')
    else:
        session.close()
        return jsonify(message='User profile not found'), 404

