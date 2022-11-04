def repr_request(r, p, cycle):
    p.text(f'{r.status_code} {r.url}\n')
    p.text('headers: ')
    for name in sorted(r.headers):
        p.text(f'  {name}: {r.headers[name]}\n')
    p.text(f"\nbody ({r.headers.get('content-type', 'unknown')}):\n")
    try:
        p.pretty(r.json())
    except ValueError:
        try:
            if len(r.text) > 1024:
                p.text(r.text[:1024])
                p.text('...[%i bytes]' % len(r.content))
            else:
                p.text(r.text)
        except Exception:
            if len(r.content) > 1024:
                p.pretty(r.content[:1024])
                p.text('...[%i bytes]' % len(r.content))
            else:
                p.pretty(r.content)

def load_ipython_extension(ip):
    ip.display_formatter.formatters['text/plain'].for_type('requests.models.Response', repr_request)
