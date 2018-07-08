import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "PATH=/usr/lib/mailman/bin:$PATH",
    ),
)
class TestInject(object):

    @pytest.mark.complete("inject ")
    def test_1(self, completion):
        assert completion.list
