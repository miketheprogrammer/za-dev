class FieldRequiredError(Exception):
    def __init__(self, message, Errors):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)

        # Now for your custom code...
        self.Errors = Errors