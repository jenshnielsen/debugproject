class Foo:
    """
    Foo is a class that does not inherit from any thing
    """

    classattr: str = "MyClassAttr"
    """
    This is a class attribute
    """

    def __init__(self):

        self.instance_attr: str = "MyInstanceAttr"
        """
        This is an instance attribute
        """


class Bar(Foo):
    """
    Bar is a class that inherits from Foo
    """

    def __init__(self):

        self.other_instance_attr: str = "MyOtherInstanceAttr"
        """
        This is annother instance attribute
        """

        super().__init__()
