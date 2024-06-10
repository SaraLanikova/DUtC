from os import environ

SESSION_CONFIGS = [
     dict(
        name='die_under_the_cup',
        display_name="Die Under the Cup",
        app_sequence=['die_under_the_cup'],
        num_demo_participants=1,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'cs' # to change ECU after the number of payoff

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'ECU' # to change points to ECU
USE_POINTS = False # to change points to ECU
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0
ECU_EXCHANGE_RATE = 1

DEBUG = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5817896459419'
