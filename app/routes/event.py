"""
Module: Event Management Routes

This module defines the endpoints for managing events in journeys.
It includes functionality for adding, editing, deleting and viewing events.
"""
from app import app
from flask import redirect, render_template, request, session, url_for, flash
from app.config import constants
from app.utils.decorators import login_required
from app.db import db
from werkzeug.utils import secure_filename
import os
from datetime import datetime

@app.route('/journey/<int:journey_id>/events')
@login_required
def view_events(journey_id):
    """View all events for a specific journey.
    
    Args:
        journey_id: The ID of the journey to view events for
    """
    with db.get_cursor() as cursor:
        # Get journey details
        cursor.execute("""
            SELECT j.*, u.username 
            FROM journeys j 
            JOIN users u ON j.user_id = u.user_id 
            WHERE j.journey_id = %s
        """, (journey_id,))
        journey = cursor.fetchone()
        
        if not journey:
            flash('Journey not found', 'error')
            return redirect(url_for('traveller_home'))
            
        # Check if user has permission to view this journey
        if journey['status'] == 'private' and journey['user_id'] != session['user_id']:
            flash('You do not have permission to view this journey', 'error')
            return redirect(url_for('traveller_home'))
            
        # Get all events for this journey
        cursor.execute("""
            SELECT * FROM events 
            WHERE journey_id = %s 
            ORDER BY start_time ASC
        """, (journey_id,))
        events = cursor.fetchall()
        
    return render_template('event/events.html', journey=journey, events=events)

@app.route('/journey/<int:journey_id>/event/add', methods=['GET', 'POST'])
@login_required
def add_event(journey_id):
    """Add a new event to a journey.
    
    Args:
        journey_id: The ID of the journey to add the event to
    """
    with db.get_cursor() as cursor:
        # Verify journey exists and user owns it
        cursor.execute("SELECT * FROM journeys WHERE journey_id = %s AND user_id = %s", 
                      (journey_id, session['user_id']))
        journey = cursor.fetchone()
        
        if not journey:
            flash('Journey not found or you do not have permission to add events', 'error')
            return redirect(url_for('traveller_home'))
            
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        location = request.form.get('location')
        
        # Validate required fields
        if not all([title, start_time, location]):
            flash('Title, start time and location are required', 'error')
            return render_template('event/event_form.html', journey=journey)
            
        # Handle image upload if provided
        event_image = None
        if 'event_image' in request.files:
            file = request.files['event_image']
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config[constants.IMAGE_UPLOAD_FOLDER], filename))
                event_image = filename
                
        with db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO events (journey_id, title, description, start_time, end_time, location, event_image)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (journey_id, title, description, start_time, end_time, location, event_image))
            
        flash('Event added successfully', 'success')
        return redirect(url_for('view_events', journey_id=journey_id))
        
    return render_template('event/event_form.html', journey=journey)

@app.route('/journey/<int:journey_id>/event/<int:event_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_event(journey_id, event_id):
    """Edit an existing event.
    
    Args:
        journey_id: The ID of the journey containing the event
        event_id: The ID of the event to edit
    """
    with db.get_cursor() as cursor:
        # Verify journey exists and user owns it
        cursor.execute("""
            SELECT j.*, e.* 
            FROM journeys j 
            JOIN events e ON j.journey_id = e.journey_id 
            WHERE j.journey_id = %s AND e.event_id = %s AND j.user_id = %s
        """, (journey_id, event_id, session['user_id']))
        event = cursor.fetchone()
        
        if not event:
            flash('Event not found or you do not have permission to edit it', 'error')
            return redirect(url_for('traveller_home'))
            
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        location = request.form.get('location')
        
        # Validate required fields
        if not all([title, start_time, location]):
            flash('Title, start time and location are required', 'error')
            return render_template('event/event_form.html', event=event)
            
        # Handle image upload if provided
        event_image = event['event_image']
        if 'event_image' in request.files:
            file = request.files['event_image']
            if file and file.filename:
                # Delete old image if it exists
                if event_image:
                    old_image_path = os.path.join(app.config[constants.IMAGE_UPLOAD_FOLDER], event_image)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                        
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config[constants.IMAGE_UPLOAD_FOLDER], filename))
                event_image = filename
                
        with db.get_cursor() as cursor:
            cursor.execute("""
                UPDATE events 
                SET title = %s, description = %s, start_time = %s, end_time = %s, 
                    location = %s, event_image = %s
                WHERE event_id = %s AND journey_id = %s
            """, (title, description, start_time, end_time, location, event_image, event_id, journey_id))
            
        flash('Event updated successfully', 'success')
        return redirect(url_for('view_events', journey_id=journey_id))
        
    return render_template('event/event_form.html', event=event)

@app.route('/journey/<int:journey_id>/event/<int:event_id>/delete', methods=['POST'])
@login_required
def delete_event(journey_id, event_id):
    """Delete an event.
    
    Args:
        journey_id: The ID of the journey containing the event
        event_id: The ID of the event to delete
    """
    with db.get_cursor() as cursor:
        # Verify journey exists and user owns it
        cursor.execute("""
            SELECT j.*, e.* 
            FROM journeys j 
            JOIN events e ON j.journey_id = e.journey_id 
            WHERE j.journey_id = %s AND e.event_id = %s AND j.user_id = %s
        """, (journey_id, event_id, session['user_id']))
        event = cursor.fetchone()
        
        if not event:
            flash('Event not found or you do not have permission to delete it', 'error')
            return redirect(url_for('traveller_home'))
            
        # Delete event image if it exists
        if event['event_image']:
            image_path = os.path.join(app.config[constants.IMAGE_UPLOAD_FOLDER], event['event_image'])
            if os.path.exists(image_path):
                os.remove(image_path)
                
        # Delete the event
        cursor.execute("DELETE FROM events WHERE event_id = %s AND journey_id = %s", 
                      (event_id, journey_id))
        
    flash('Event deleted successfully', 'success')
    return redirect(url_for('view_events', journey_id=journey_id)) 