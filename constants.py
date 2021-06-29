
# ===== regexes =====
UUID_REGEX = r'^[a-z0-9]*\-[a-z0-9\-]*$'
AUTH_TOKEN_REGEX = r'^Bearer [a-zA-Z0-9]+$'
DATE_REGEX = r'^\d\d\-\d\d\-\d\d\d\d$'
EMAIL_REGEX = r'[a-zA-z0-9\-\_\.]+@[a-zA-z0-9\-\_\.]+\.[a-zA-z0-9\-\_\.]+'

# ===== routes =====
SAMPLE_ROUTE = '/sample'
MODEL_ROUTE = '/model'

# ===== paths =====
MODELS_PATH = 'data/models.json'

# ===== value types =====
STRING = "String"
LIST = "List"
BOOLEAN = "Boolean"
INT = "Int"
DATE = "Date"
UUID = "UUID"
EMAIL = "Email"
AUTH_TOKEN = "Auth-Token"

# ===== constants =====
TYPE_MISMATCH = 'type mismatch'
MISSING_REQUIRED = 'missing required parameter'
HEADERS = 'headers'
BODY = 'body'
QUERY_PARAMS = 'query_params'
METHOD = 'method'
PATH = 'path'
PART = 'part'
TYPE = 'type'
FIELD = 'field'
POSSIBLE_TYPES = 'possible_types'
TYPES = 'types'
ABNORMAL = 'abnormal'
ABNORMALITIES = 'abnormalities'
VALUE = 'value'
REQUIRED = 'required'
NAME = 'name'
