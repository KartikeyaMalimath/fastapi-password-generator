import secrets
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import string

from starlette.responses import JSONResponse

router = APIRouter()

DEFAULT_CHARACTERS = string.ascii_letters + string.digits + string.punctuation


class PasswordRequest(BaseModel):
    length: int
    exclude_uppercase: Optional[bool] = Field(False, description="Pass True to exclude uppercase characters in the password.")
    exclude_lowercase: Optional[bool] = Field(False, description="Pass True to exclude lowercase characters in the password.")
    exclude_numbers: Optional[bool] = Field(False, description="Pass True to exclude numbers in the password.")
    exclude_special_characters: Optional[bool] = Field(False, description="Pass True to exclude all special characters in the password.")
    exclude_characters: Optional[str] = Field("", description="Pass characters to be excluded in the password.")
    custom_characters: Optional[str] = Field(None, description="Pass custom characters to include at least one custom character in the password.")
    passphrase: Optional[str] = Field(None, description="Pass a passphrase to be used as seed to generate the password.")


def generate_default_password(length):
    """
    Generate a default password that includes:
    (DEFAULT_CHARACTERS) uppercase-lowercase letters, numbers and special characters .

    Parameters:
    - length (int): The length of the password to generate.

    Returns:
    - str: The generated default password.
    """
    return ''.join(secrets.choice(DEFAULT_CHARACTERS) for _ in range(length))


def generate_custom_password(request, length, allowed_characters):
    """
    Generate a custom password based on the allowed character types.

    Parameters:
    - request (PasswordRequest): The request containing password generation parameters.
    - length (int): The length of the password to generate.
    - allowed_characters (str): The set of allowed characters.

    Returns:
    - str: The generated custom password.
    """
    password = ''.join(secrets.choice(allowed_characters) for _ in range(length))

    if request.custom_characters and not any(char in password for char in request.custom_characters):
        password = password[:length - 1] + secrets.choice(request.custom_characters)

    return password


def validate_request(request):
    """
    Validate the password request.

    Parameters:
    - request (PasswordRequest): The password request to validate.

    Raises:
    - HTTPException: If the password length is less than 8.
    """
    if request.length < 8:
        raise HTTPException(status_code=400, detail="Password length should be a minimum of 8")
    if request.length > 256:
        raise HTTPException(status_code=400, detail="Password length should be a maximum of 256")


def get_allowed_characters(request):
    """
    Get the allowed characters based on the request.

    Parameters:
    - request (PasswordRequest): The password request.

    Returns:
    - str: The set of allowed characters.
    """
    allowed_characters = []

    if not request.exclude_uppercase:
        allowed_characters.extend(string.ascii_uppercase)
    if not request.exclude_lowercase:
        allowed_characters.extend(string.ascii_lowercase)
    if not request.exclude_numbers:
        allowed_characters.extend(string.digits)
    if not request.exclude_special_characters:
        allowed_characters.extend(string.punctuation)
    if request.exclude_characters:
        allowed_characters = [char for char in allowed_characters if char not in request.exclude_characters]
    if request.custom_characters:
        allowed_characters.extend([char for char in request.custom_characters])

    if not allowed_characters:
        raise HTTPException(status_code=400, detail="At least one character type should be included")

    allowed_characters_str = ''.join(allowed_characters)
    return allowed_characters_str


@router.post("/generate-password", response_model=dict)
def generate_password(request: PasswordRequest):
    """
    Generate a password based on the provided request.

    Parameters:
    - request (PasswordRequest): The request containing password generation parameters.

    Returns:
    - JSONResponse: The JSON response containing the generated password.
    """
    validate_request(request)

    if request.passphrase:
        random_generator = secrets.SystemRandom()
        random_generator.seed(request.passphrase)

    allowed_characters = get_allowed_characters(request) if any([
        not request.passphrase,
        request.exclude_uppercase,
        request.exclude_lowercase,
        request.exclude_numbers,
        request.exclude_special_characters,
        request.custom_characters,
        request.exclude_characters
    ]) else DEFAULT_CHARACTERS

    generated_password = generate_custom_password(request, request.length, allowed_characters)

    return JSONResponse({"password": generated_password})

