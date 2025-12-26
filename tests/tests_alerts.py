from bot.alert_manager import should_trigger

def test_trigger_above_true():
    assert should_trigger(105, 100, "above") is True

def test_trigger_above_false():
    assert should_trigger(95, 100, "above") is False

def test_trigger_below_true():
    assert should_trigger(90, 100, "below") is True

def test_trigger_below_false():
    assert should_trigger(110, 100, "below") is False

def test_invalid_condition():
    assert should_trigger(100, 100, "invalid") is False
