from fastapi import HTTPException, status
from fastapi.routing import APIRouter

from app.schema.schemas import Otp, UserRequest
from app.utils.otp import create_otp, verify_otp


from fastapi import FastAPI, Request, Form

from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import smtplib
from email.message import EmailMessage

router = APIRouter(tags=["notification"])


@router.post("/create_otp", status_code=status.HTTP_201_CREATED)
async def generate_otp(data: UserRequest):
    await create_otp(data.id)
    return f"otp was sent to {data.username}"


@router.post("/verify_otp", status_code=status.HTTP_200_OK)
async def verify(data: Otp):
    result = await verify_otp(data.otp)
    return result


@router.post("/submit")
async def submit(name: str = Form(), emailAddress: str = Form(), message: str = Form()):
    print(name)
    print(emailAddress)
    print(message)

    email_address = "sinaleylaz999@gmail.com"  # type Email
    email_password = "tlsgiupignycbpyn"  # If you do not have a gmail apps password, create a new app with using generate password. Check your apps and passwords https://myaccount.google.com/apppasswords

    # create email
    msg = EmailMessage()
    msg["Subject"] = "Email subject"
    msg["From"] = email_address
    msg["To"] = "clydeymojica0130@gmail.com"  # type Email
    msg.set_content(
        f"""\
    Name : {name}
    Email : {emailAddress}
    Message : {message}    
    """,
    )
    # send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    return "email successfully sent"
