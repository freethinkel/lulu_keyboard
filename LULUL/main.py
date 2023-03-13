from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.extensions.media_keys import MediaKeys
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
media_keys = MediaKeys()

keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
keyboard.extensions.append(media_keys)

oled_ext = Oled(OledData(image={0:OledReactionType.LAYER,1:["1.bmp","2.bmp","3.bmp","4.bmp","5.bmp","6.bmp","7.bmp","8.bmp"]}),toDisplay=OledDisplayMode.IMG,flip= True)
keyboard.extensions.append(oled_ext)
split = Split(use_pio=True)
keyboard.modules.append(split)

keyboard.keymap = [ 
[
KC.ESCAPE,   KC.N1,    KC.N2,    KC.N3,    KC.N4,   KC.N5,                                      KC.N6,     KC.N7,    KC.N8,     KC.N9,   KC.N0,     KC.BSPC,
KC.TAB,      KC.Q,     KC.W,     KC.E,     KC.R,    KC.T,                                       KC.Y,      KC.U,     KC.I,      KC.O,    KC.P,      KC.MINUS,
KC.LCTRL,    KC.A,     KC.S,     KC.D,     KC.F,    KC.G,                                       KC.H,      KC.J,     KC.K,      KC.L,    KC.SCOLON, KC.QUOTE,
KC.LSHIFT,   KC.Z,     KC.X,     KC.C,     KC.V,    KC.B,     KC.LBRACKET,        KC.RBRACKET,  KC.N,      KC.M,     KC.COMMA,  KC.DOT,  KC.SLASH,  KC.RSHIFT,
                                 KC.MO(1), KC.LALT, KC.LGUI,  KC.SPACE,            KC.ENTER,     KC.BSPC,   KC.RGUI,  KC.MO(1),
], 

[
 KC.BRID,  KC.BRIU,  KC.F3,    KC.F4,    KC.F5,    KC.F6,                                   KC.MRWD,  KC.MPLY,   KC.MFFD,  KC.MUTE,  KC.VOLD,  KC.VOLU,
 KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                                 KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.EQUAL, KC.TRNS,
 KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                                 KC.LEFT,  KC.DOWN,   KC.UP,    KC.RIGHT, KC.TRNS,  KC.TRNS,
 KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.GRAVE,          KC.BSLASH,  KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                               KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,           KC.TRNS,    KC.TRNS,  KC.DELETE, KC.TRNS
],

[
KC.N2,    KC.EXCLAIM,  KC.AT,   KC.HASH,  KC.DOLLAR,  KC.PERCENT,                                                      KC.CIRCUMFLEX,  KC.AMPERSAND,  KC.ASTERISK,            KC.LEFT_PAREN,           KC.RIGHT_PAREN,  KC.TILDE,
KC.TRNS,  KC.TRNS,     KC.TRNS, KC.TRNS,  KC.TRNS,    KC.TRNS,                                                         KC.TRNS,        KC.TRNS,       KC.TRNS,                KC.TRNS,                 KC.PLUS,         KC.UNDERSCORE,
KC.TRNS,  KC.TRNS,     KC.TRNS, KC.TRNS,  KC.TRNS,    KC.TRNS,                                                         KC.TRNS,        KC.TRNS,       KC.TRNS,                KC.TRNS,                 KC.COLON,        KC.DOUBLE_QUOTE,
KC.TRNS,  KC.TRNS,     KC.TRNS, KC.TRNS,  KC.TRNS,    KC.TRNS,  KC.LEFT_CURLY_BRACE,            KC.RIGHT_CURLY_BRACE,  KC.TRNS,        KC.TRNS,       KC.LEFT_ANGLE_BRACKET,  KC.RIGHT_ANGLE_BRACKET,  KC.QUESTION,     KC.TRNS,
                                KC.LGUI,  KC.TRNS,    KC.TRNS,  KC.TRNS,                        KC.TRNS,               KC.TRNS,        KC.TRNS,       KC.RIGHT_CURLY_BRACE,
], 

[
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
],

[
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
],

[
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
],

[
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
],

[
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                         KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
],
]

# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)
