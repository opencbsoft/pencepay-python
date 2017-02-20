import pytest

from pencepay.settings.config import Context


class TestContext:
    def test_error_raises_when_setting_dynamic_attribute(self):
        context = Context()

        with pytest.raises(TypeError):
            context.something = '123'

    def test_error_raises_when_setting_dynamic_attribute_to_class(self):
        with pytest.raises(TypeError):
            Context.something = '123'

    def test_set_api_version(self):
        Context.set_api_version('1')

        assert Context.api_version == '1'

    def test_set_public_key(self):
        Context.set_public_key('some_public_key')

        assert Context.public_key == 'some_public_key'

    def test_set_secret_key(self):
        Context.set_secret_key('some_secret_key')

        assert Context.secret_key == 'some_secret_key'
