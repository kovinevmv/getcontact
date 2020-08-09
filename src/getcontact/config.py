class Config:
    """
    Change TOKEN, AES_KEY, PRIVATE_KEY to your in tokens.yaml.
    Find it in /data/data/app.source.getcontact/shared_prefs/GetContactSettingsPref.xml
    Required ROOT on your device.

    Actual settings information at time of GetContact application version 4.9.1

    Other parameters can be changed as desired or if script does not work with default values :)

    * TOKEN: TOKEN
    * AES_KEY: FINAL_KEY
    * PRIVATE_KEY: PRIVATE_KEY
    * APP_VERSION: version of installed GetContact apk.
    * API_VERSION: API version of current app, can be found in intercepted packets
    * ANDROID_OS: version of your Android OS, can be found in intercepted packets
    * DEVICE_ID: ID of your ANDROID device, can be found in intercepted packets or *#*#8255#*#*
    * COUNTRY: country
    * HMAC_KEY: HMAC key for generation secure data sending
    * MOD_EXP: Mod exponent or AES key generation
    """

    # Will be changed using dump/tokens.yaml data
    TOKEN = "hphofd5757307f5dbffce25ae9ef4bd54dc56e770bc763215e7dc4f02e3"
    AES_KEY = "764fe50cdb21a07c4c049377754c2f50f127febb3aa67e03c7334f414e0fa7db"
    PRIVATE_KEY = 1  # exp

    # May need to be changed
    APP_VERSION = "4.9.1"
    API_VERSION = "v2.5"
    ANDROID_OS = "android 5.0"
    DEVICE_ID = "8edbe110a4079829"

    # Default values
    COUNTRY = "RU"
    HMAC_KEY = "2Wq7)qkX~cp7)H|n_tc&o+:G_USN3/-uIi~>M+c ;Oq]E{t9)RC_5|lhAA_Qq%_4"
    MOD_EXP = 900719925481

    VERBOSE = False


config = Config()
