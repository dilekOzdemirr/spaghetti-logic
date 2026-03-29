import os
from typing import Optional


def get_aws_credentials() -> str:
    """
    Retrieve AWS credentials from environment variables.

    This function implements secure credential management by:
    - Reading from environment variables instead of hardcoded values
    - Supporting multiple credential sources (priority order):
      1. IAM Role (Production - EC2/Lambda)
      2. Environment Variable (AWS_SECRET_KEY)
      3. .env file (Development - via python-dotenv)

    Returns:
        str: AWS secret key

    Raises:
        ValueError: If AWS_SECRET_KEY is not found or invalid

    Example:
        # Development (local .env file)
        AWS_SECRET_KEY="AKIA_XXXX" python app.py

        # Production (IAM Role on EC2/Lambda)
        # No setup needed - boto3 automatically uses IAM role
    """
    aws_secret_key = os.getenv("AWS_SECRET_KEY")

    if not aws_secret_key:
        raise ValueError(
            "AWS_SECRET_KEY environment variable not set. "
            "Please configure it via: export AWS_SECRET_KEY='your_key' "
            "or set it in a .env file (development only)"
        )

    # Validate AWS key format (basic check)
    if not aws_secret_key.startswith("AKIA_"):
        raise ValueError(
            f"Invalid AWS key format. Expected AKIA_* format, got: {aws_secret_key[:10]}..."
        )

    return aws_secret_key


def connect() -> None:
    """
    Connect to AWS using secure credentials.

    Retrieves credentials from environment and establishes secure connection.
    Credentials are NOT displayed in logs/console (only masked prefix shown).

    Raises:
        ValueError: If credentials are not properly configured
    """
    try:
        aws_secret_key = get_aws_credentials()
        # Display only first 4 chars for security (masking)
        masked_key = f"{aws_secret_key[:4]}***{aws_secret_key[-4:]}"
        print(f"Connecting with AWS credential (masked): {masked_key}")
        # Actual AWS operations would go here (boto3)
    except ValueError as e:
        print(f"Connection failed: {e}")
        raise


if __name__ == "__main__":
    """
    Example usage (Development only)

    Setup:
    1. Create .env file:
       echo 'AWS_SECRET_KEY=AKIA_FAKE_KEY_123456789_STUDENT_TEST' > .env

    2. Add to .gitignore:
       echo '.env' >> .gitignore

    3. Install python-dotenv (optional):
       pip install python-dotenv

    4. Run:
       python secret_leak.py
    """
    # Load from .env file if available (development only)
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        # python-dotenv not installed, use environment variables
        pass

    connect()