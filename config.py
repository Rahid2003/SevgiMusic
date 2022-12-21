from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgC0uWq2nnrxHaHmv97dhbzqC6eyx9TLVL-uiZZitcgLrBkFXgrrbgf25raPVURHDEo945qQSZPBIoHgPgbLVi1e1N0o9bIdRnGbhdmD0j3vg4UA_NCLycnE9HOB9Z8WMOI9Y8w-oMqhuO0qDRU6k9SzFWbWgHkKZWDCn1SITHIzGDOdyVnp6y3NYtU9EazImSUUYYg06gPv5zJ-jU7sI2yiOELHlM7XYSWT0rcxU-BmxTTM9377tsUU7FNn0x1Z4BrmjBAhi5E0SStmmqfUPkYflItN9Q0vV0qxlf60ywcOJjobh44tMShPccqi2q15_kMx9ZL5-M3_C5pG1sTQchLsAAAAAU87jeQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5461712721:AAFHX821IrwbRa0EA8bpezz08ASMiifGFlQ")
BOT_NAME = getenv("BOT_NAME", "𝑴𝑺 ~ 𝑴𝒖𝒔𝒊𝒄") 
API_ID = int(getenv("API_ID", "19485442"))
API_HASH = getenv("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
BOT_USERNAME = getenv("BOT_USERNAME", "Sevgi_Music_Bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5451034037").split()))
