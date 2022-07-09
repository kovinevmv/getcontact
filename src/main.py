import argparse

from getcontact.getcontact import GetContactAPI
from getcontact.config import config

description = "Get information about phone number from databases of GetContact"

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-p",
                    "--phone",
                    help="Phone number (example: +78005553535)")
parser.add_argument("-j",
                    "--json",
                    help="Print output in JSON format",
                    action="store_true")
parser.add_argument("-v", "--verbose", help="Log", action="store_true")

args = parser.parse_args()

phone = args.phone
getcontact = GetContactAPI()
config.VERBOSE = args.verbose

if args.json:
    print(getcontact.get_information_by_phone(phone))
else:
    getcontact.print_information_by_phone(phone)
