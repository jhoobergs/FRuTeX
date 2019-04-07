import frutex_parser


attrib_dict = {
        "content": "content",
        "color"  : "color",
        }

attrib_to_default_dict = {
        "content": "default_content",
        "color": "default_color",
        }

default_config = {
        "default_content": frutex_parser.NoneExpr(),
        "default_color" : frutex_parser.Integer(0xffd750),
        "default_width" : "75",
        "default_height" : "30",
        "num_rows" : "20",
        "num_cols" : "20",
}