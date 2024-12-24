from testpkg import trace

def test_testpkg(caplog):
    trace('test trace message')
    assert 'test trace message' in caplog.text