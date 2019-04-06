
attrib_dict = {
        "content": "content",
        "color"  : "color",
        }

attrib_to_default_dict = {
        "content": "default_content",
        "color": "default_color",
        }

default_config = {
        "default_content": "None",
        "default_color" : "0xffd750",
        "default_width" : "75",
        "default_height" : "30",
        "num_rows" : "20",
        "num_cols" : "20",
}

LETTERS           = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_UND       = LETTERS + '_'
NUMBERS           = "0123456789"
LETTERS_NUMS_UND  = LETTERS_UND + NUMBERS

OPERATOR_CHARS    = "+-*/%!=><"
OPERATOR_DICT     = {"+":"",
                     "-":"",
                     "*":"*",
                     "/":"/",
                     "%":"",
                     "!":"=",
                     "=":"=",
                     ">":"=",
                     "<":"="}

OPERATOR_ORDER    = (
        ('*', '/', '//'),
        ('+', '-'),
)
    
    