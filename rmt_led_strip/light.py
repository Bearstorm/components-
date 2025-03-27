import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.const import CONF_ID, CONF_PIN, CONF_NUM_LEDS, CONF_NAME

AUTO_LOAD = ['light']
CODEOWNERS = [""]

rmt_led_strip_ns = cg.esphome_ns.namespace('rmt_led_strip')
RMTLedStripLight = rmt_led_strip_ns.class_('RMTLedStripLight', light.AddressableLight)

CONFIG_SCHEMA = light.ADDRESSABLE_LIGHT_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(RMTLedStripLight),
    cv.Required(CONF_PIN): cv.pin,
    cv.Required(CONF_NUM_LEDS): cv.int_range(min=1),
    cv.Optional("chipset", default="ws2812"): cv.string_strict,
    cv.Optional("rgb_order", default="GRB"): cv.string_strict,
    cv.Optional("rmt_channel", default=0): cv.int_range(min=0, max=7),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield light.register_light(var, config)
    cg.add(var.set_pin(config[CONF_PIN]))
    cg.add(var.set_num_leds(config[CONF_NUM_LEDS]))
    cg.add(var.set_chipset(config["chipset"]))
    cg.add(var.set_rgb_order(config["rgb_order"]))
    cg.add(var.set_rmt_channel(config["rmt_channel"]))
