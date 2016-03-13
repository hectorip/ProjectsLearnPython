canUpdate = lambda n, o, c, u: l(n) == l(o) or not(c or re.search('\W', n) or l(n) in map(l,u))
l = unicode.lower