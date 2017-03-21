import time
from sys import exit

positive=["ja", "yes", "yep", "of course", "indeed", "definitely", "absolutely"]
negative=["no", "nope", "nein", "nay", "not"]
not_understood = "I didn\'t get that, sorry"

def define_listener():
    print "Hey! This is FakeLocate."
    print "What is your name?"
    define_listener.player_name = raw_input(">>> ")
    print "Ok, cool, %r." % define_listener.player_name
    print "Let me tell you about my Project:"
    time.sleep(3)
    fail()

def fail():
    print "The original idea was to make FakeLocate an App or something close to that."
    time.sleep(4)
    print "Well, I failed."
    time.sleep(2)
    print "Nevertheless, some interesting thoughtwork and ideas came up."
    time.sleep(2)
    print "Will you listen to me anyway?"

    while True:
        fail_decision = raw_input(">>> ").lower()
        if fail_decision in positive:
            print "Nice, thanks, let\'s proceed."
            explanation()
        elif fail_decision in negative:
            print "Well, then don\'t!"
            time.sleep(2)
            exit(0)
        else:
            print not_understood

def explanation():
    print """So %r, what I wanted to achieve, is a program that can do
    two things:""" % define_listener.player_name
    time.sleep(4)
    print "First: It should be able to wipe all EXIF data from a photo."
    print """Then it should add randomized EXIF data in order to confuse anyone
    who tries to extract personal data from an image file. Therefor,
    FakeLocate creates awareness about personal data stored in image files."""
    time.sleep(5)
    print """Second: FakeLocate is an app that has destructive potential, too.
    It was going to have an *INSANE* mode, which again randomly adds EXIF data
    to a file and then uploads that file to multiple platforms."""
    time.sleep(5)
    print """Many of those platforms, like Google e.g. try to fetch geolocations
    from EXIF data of images and assign those files to a certain location on a map.
    FakeLocate messes with that kind of information, so the image of that dumpster
    near your home will suddenly appear on Champs-Elysees in Paris."""
    time.sleep(5)
    print """Wow, lots of information, so could you follow me until now?"""

    while True:
        fail_decision = raw_input(">>> ").lower()

        if fail_decision in positive:
            print "Great, so lets move to the more technical part."
            technical_part()
        elif fail_decision in negative:
            print """Well, %r, Sorry to hear, maybe you should listen
             again""" % define_listener.player_name
            time.sleep(2)
            explanation()
        else:
            print not_understood


def technical_part():
    time.sleep(4)
    print """The way to go for me was to begin with the direct image uploading
    function of Dropbox, a service I use quite a lot."""
    print """The uploading function allows to get images onto a server directly,
    without any further ado."""
    time.sleep(5)
    print """Now, the plan was to write a python script that could access those
    files directly, take care of the EXIF data and leave those in the user\'s
    Dropbox"""
    time.sleep(5)
    print """The way to go with that is a library called PyExifTool, which
    is a wrapper that implements a command-line application into Python."""
    print """The problem with that is, that the workflow with this wrapper was
    a lot harder than I expected; its syntax is very unintuitive."""
    print """I managed to do all I wanted for the EXIF data in the command-line,
    but for the python wrapper, this was something I couldn\'t quite figure out."""
    time.sleep(5)
    print """The next problem I ran into, was Google's and other services own
    uploading procedures. It turned out to be impossible to just automate
    uploads without any restrictions and they wouldn\'t show up online."""
    time.sleep(5)
    print """Finally, I decided to make a prototype that showed what the app
    could do and would look like, rather than actually going into programming
    it, it was just a little bit too complicated for me, I hope you understand
    %r!""" % define_listener.player_name
    time.sleep(6)
    print """I included a video of how my App could work in the Readme.md, hope
    you have fun watching it. Thanks for playing,"""
    time.sleep(3)
    print "all the best,"
    print "Henri"
    exit(0)

define_listener()
