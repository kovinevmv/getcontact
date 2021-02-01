class Config:
    """
    Change TOKEN, AES_KEY to your in tokens.yaml.
    Find it in /data/data/app.source.getcontact/shared_prefs/GetContactSettingsPref.xml
    Required ROOT on your device.

    Actual settings information at time of GetContact application version 4.9.1

    Other parameters can be changed as desired or if script does not work with default values :)

    * TOKEN: TOKEN
    * AES_KEY: FINAL_KEY
    * APP_VERSION: version of installed GetContact apk.
    * API_VERSION: API version of current app, can be found in intercepted packets
    * ANDROID_OS: version of your Android OS, can be found in intercepted packets
    * DEVICE_ID: ID of your ANDROID device, can be found in intercepted packets or *#*#8255#*#*
    * COUNTRY: country
    * HMAC_KEY: HMAC key for generation secure data sending
    * MOD_EXP: Mod exponent or AES key generation
    """

    # Will be changed using dump/tokens.yaml data
    TOKEN = "rJrKc01a26b9a013ff3a35f6753820971f63c3f9f8571c8012e3c9633ba"
    AES_KEY = "dd074ed6e8c64bc65cabdfdca052f16b187e5cbbc501e22d98dae2f9899fe543"

    # May need to be changed
    APP_VERSION = "4.9.1"
    API_VERSION = "v2.8"
    ANDROID_OS = "android 6.0"
    DEVICE_ID = "8edbe110a4079830"

    # Default values
    COUNTRY = "RU"
    HMAC_KEY = "2Wq7)qkX~cp7)H|n_tc&o+:G_USN3/-uIi~>M+c ;Oq]E{t9)RC_5|lhAA_Qq%_4"
    MOD_EXP = 900719925481

    VERBOSE = False


config = Config()
