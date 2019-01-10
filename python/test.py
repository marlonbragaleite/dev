import urwid

txt = urwid.Text(u"Hello")
fill = urwid.Filler(txt, 'middle')
loop = urwid.MainLoop(fill)
loop.run()

