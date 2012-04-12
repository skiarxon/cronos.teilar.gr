#!/usr/bin/env python

from distutils.core import setup

datadir = "/lib$ARCH/python$(python_get_version)/site-packages/${PN}"

setup(
    name="cronos",
    version="0.3",
    description="cronos.teilar.gr website",
    url="git://linuxteam.teilar.gr/cronos.git",
    author="Cronos Development Team",
    author_email="cronos@teilar.gr",
    license="AGPLv3",
    packages=['cronos', 'cronos.accounts', 'cronos.announcements', 'cronos.cron',
		'cronos.dionysos', 'cronos.eclass', 'cronos.libraries',   'cronos.library',
		'cronos.login', 'cronos.teachers', 'cronos.webmail'],
    package_dir = {'cronos':'cronos'},
    data_files = [
        (datadir + "css",
            ["cronos/css/reset.css", "cronos/css/style.css", "cronos/css/style_intro.css"]),
        (datadir + "js",
            ["cronos/js/multibox.js"]),
        (datadir + "img",
            ["cronos/img/button_bg_link.png", "cronos/img/button_bg_over.png", "cronos/img/cid0.png",
            "cronos/img/cid50.png", "cronos/img/cid51.png", "cronos/img/cid52.png",
            "cronos/img/cid53.png", "cronos/img/cid54.png", "cronos/img/cid55.png",
            "cronos/img/department.png", "cronos/img/eclass.png", "cronos/img/header_bg.png",
            "cronos/img/login_bg.png", "cronos/img/logo_bg.png", "cronos/img/logo_login.png",
            "cronos/img/logo.png", "cronos/img/logo_sidebar.png", "cronos/img/meeting.png",
            "cronos/img/navigation_bg_active.png", "cronos/img/navigation_bg_link.png",
            "cronos/img/navigation_bg_over.png", "cronos/img/note_blank.png", "cronos/img/note_blank.png",
            "cronos/img/pid323.png", "cronos/img/pid324.png", "cronos/img/profile_bg.jpg",
            "cronos/img/rss.png", "cronos/img/teacher.png", "cronos/img/teachers.png",
            "cronos/img/src/logo_login.xcf", "cronos/img/src/logo_side.xcf",
            "cronos/img/src/note_blank.svg", "cronos/img/src/note.xcf"]),
        (datadir + "others",
            ["cronos/others/apache.conf", "cronos/others/robots.txt"]),
        (datadir + "templates",
            ["cronos/templates/404.html", "cronos/templates/500.html", "cronos/templates/about.html",
            "cronos/templates/announcements.html", "cronos/templates/base.html", "cronos/templates/dionysos.html",
            "cronos/templates/eclass.html", "cronos/templates/index.html", "cronos/templates/intro.html",
            "cronos/templates/library.html", "cronos/templates/login.html", "cronos/templates/preferences.html",
            "cronos/templates/psigeia.html", "cronos/templates/recover.html", "cronos/templates/signup.html",
            "cronos/templates/teachers.html", "cronos/templates/webmail.html", "cronos/templates/welcome.html",
            "cronos/templates/feeds/announcements_description.html", "cronos/templates/feeds/announcements_title.html"]),
    ],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: AGPLv3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["django", "cronos", "teilar", "thesis", "larissa"]
)
