def PublicViews(route):

    @route("/")
    def hello():
        return "Hi!"

    @route("/<int:number>")
    def number(number):
        return str(number)
