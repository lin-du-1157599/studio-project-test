# Used to indicate whether the user is logged in in the session
SESSION_LOGGED_IN = 'loggedin'

HTTP_METHOD_POST = 'POST'
HTTP_METHOD_GET = 'GET'

# Role to new users upon registration.
USER_ROLE_TRAVELLER = 'traveller'
USER_ROLE_EDITOR = 'editor'
USER_ROLE_ADMIN = 'admin'

# User information fields
USER_ID = 'user_id'  # Unique identifier for the user
USERNAME = 'username' 
USER_ROLE = 'role'
EMAIL = 'email'
PASSWORD_HASH = 'password_hash'
RE_PASSWORD = 'repassword'
PASSWORD = 'password'
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
LOCATION = 'location'
USER_STATUS='status'
USER_PROFILE_IMAGE='profile_image'
USER_FULL_NAME = 'full_name'
USER_PERSONAL_DESCRIPTION = 'personal_description'


DEFAULT_USER_ROLE = 'traveller'
DEFAULT_STATUS = 'active'

# user status
USER_STATUS_ACTIVE = 'active'
USER_STATUS_BANNED = 'banned'

IMAGE_UPLOAD_FOLDER = 'IMAGE_UPLOAD_FOLDER'
IMAGE_UPLOAD_FOLDER_URL = 'static/uploads'

# URL endpoint names
URL_LOGIN = 'login'  # URL for the login page
URL_TRAVELLER_HOME = 'traveller_home'
URL_EDITOR_HOME = 'editor_home'
URL_ADMIN_HOME = 'admin_home'
URL_PROFILE = 'profile'
URL_SIGNUP = 'signup'

# Event-related URLs
URL_VIEW_EVENTS = 'view_events'
URL_ADD_EVENT = 'add_event'
URL_EDIT_EVENT = 'edit_event'
URL_DELETE_EVENT = 'delete_event'

# Template file names
TEMPLATE_ACCESS_DENIED = 'access_denied.html'  # Template displayed when a user is denied access to a resource
TEMPLATE_ADMIN_HOME = 'admin_home.html'  # Template for the admin home page
TEMPLATE_EDITOR_HOME = 'editor_home.html'  # Template for the editor home page
TEMPLATE_TRAVELLER_HOME = 'traveller_home.html'  # Template for the traveller home page
TEMPLATE_LOGIN= 'login.html'
TEMPLATE_USER = 'users.html'
TEMPLATE_USER_EDIT = 'user_edit.html'
TEMPLATE_SIGN_UP = 'signup.html'
TEMPLATE_PROFILE = 'profile.html'
TEMPLATE_CHANGE_PASSWORD = 'change_password.html'
TEMPLATE_AVATAR_PREVIEW = 'avatar_preview.html'

# Event-related templates
TEMPLATE_EVENTS = 'event/events.html'
TEMPLATE_EVENT_FORM = 'event/event_form.html'

# HTTP status codes
# User permission-related issues
HTTP_STATUS_CODE_403 = 403  # Forbidden: User does not have permission to access the requested resource
# Database errors or other internal server issues
HTTP_STATUS_CODE_500 = 500  # Internal Server Error: A generic error indicating that something went wrong on the server side
HTTP_STATUS_CODE_404 = 404

# Flash message types for different scenarios
FLASH_MESSAGE_DANGER = 'danger' # Used for error messages or warnings

SEARCH_TERM = 'searchterm'  # Query parameter for the search term
SEARCH_CATEGORY = 'searchcat'  # Query parameter for the search category

FORM_FIELD_CURRENT_PASSWORD = 'current_password'  # Form field for the user's current password
FORM_FIELD_NEW_PASSWORD = 'new_password'  # Form field for the user's new password
FORM_FIELD_CONFIRM_PASSWORD = 'confirm_password'  # Form field to confirm the new password
FORM_FIELD_FIRSTNAME = 'firstname'
FORM_FIELD_LASTNAME = 'lastname'
FORM_FIELD_CONFIRM_PASSWORD = 'confirm_password'


