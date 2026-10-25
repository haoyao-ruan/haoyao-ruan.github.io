# Section illustrations, unDraw style (faceless, flat). Run: python3 scripts/illustrations.py
ACC="#6c5ce7"; ACCL="#b8b0ff"; SKIN="#f1c9ad"; HAIR="#1f1d2b"; NAVY="#1e2340"; NAVY2="#2b3158"
GREY="#dfe3ea"; GREY2="#c3c9d4"; WHITE="#ffffff"; DARK="#1a1c2c"

def svg(w,h,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">\n{body}\n</svg>'

def head(x,y,s=1.0):
    # faceless head with chin length bob and soft bangs; x,y = centre of face
    return f'''<g transform="translate({x},{y}) scale({s})">
  <path d="M-27,-4 C-30,-46 30,-46 27,-4 L30,30 C31,38 20,40 16,32 L-16,32 C-20,40 -31,38 -30,30 Z" fill="{HAIR}"/>
  <ellipse cx="0" cy="6" rx="18" ry="22" fill="{SKIN}"/>
  <path d="M-21,2 C-24,-34 24,-34 21,2 C18,-10 10,-16 0,-16 C-10,-16 -18,-10 -21,2 Z" fill="{HAIR}"/>
  <path d="M-21,0 C-24,12 -22,24 -15,32 L-9,32 C-14,22 -15,10 -13,0 Z" fill="{HAIR}"/>
  <path d="M21,0 C24,12 22,24 15,32 L9,32 C14,22 15,10 13,0 Z" fill="{HAIR}"/>
</g>'''

# ---------- intro: sitting on the desk edge, legs crossed, monitor at right ----------
intro = svg(520,360,f'''
<!-- desk -->
<rect x="150" y="232" width="340" height="12" rx="3" fill="{GREY2}"/>
<rect x="420" y="244" width="70" height="116" fill="{GREY}"/>
<rect x="432" y="262" width="46" height="6" rx="3" fill="{NAVY}"/><rect x="432" y="296" width="46" height="6" rx="3" fill="{NAVY}"/><rect x="432" y="330" width="46" height="6" rx="3" fill="{NAVY}"/>
<rect x="222" y="244" width="78" height="116" fill="{GREY}"/>
<rect x="236" y="262" width="50" height="6" rx="3" fill="{NAVY}"/><rect x="236" y="296" width="50" height="6" rx="3" fill="{NAVY}"/><rect x="236" y="330" width="50" height="6" rx="3" fill="{NAVY}"/>
<!-- monitor -->
<rect x="318" y="118" width="124" height="86" rx="6" fill="{NAVY}"/>
<rect x="324" y="124" width="112" height="70" rx="3" fill="{WHITE}"/>
<g fill="{ACC}">
<rect x="334" y="136" width="30" height="5" rx="2"/><rect x="370" y="136" width="18" height="5" rx="2"/><rect x="394" y="136" width="26" height="5" rx="2"/>
<rect x="340" y="148" width="22" height="5" rx="2"/><rect x="368" y="148" width="40" height="5" rx="2"/>
<rect x="340" y="160" width="46" height="5" rx="2"/><rect x="392" y="160" width="14" height="5" rx="2"/>
<rect x="334" y="172" width="18" height="5" rx="2"/><rect x="358" y="172" width="34" height="5" rx="2"/><rect x="398" y="172" width="22" height="5" rx="2"/>
</g>
<rect x="372" y="204" width="16" height="18" fill="{NAVY}"/><rect x="352" y="220" width="56" height="8" rx="3" fill="{NAVY}"/>
<rect x="306" y="222" width="30" height="8" rx="3" fill="{NAVY2}"/>
<!-- back leg: hanging straight down -->
<path d="M214,236 L204,338" stroke="{NAVY}" stroke-width="24" stroke-linecap="round" fill="none"/>
<path d="M196,336 C188,338 178,346 182,354 L214,354 L212,336 Z" fill="{DARK}"/>
<!-- torso: open jacket over an accent top, slight slouch -->
<path d="M192,242 C184,204 188,152 208,126 L242,126 C260,152 262,204 250,242 Z" fill="{NAVY}"/>
<path d="M214,130 L238,130 C240,170 238,212 236,242 L218,242 C214,212 212,170 214,130 Z" fill="{ACC}"/>
<path d="M208,126 L218,130 C208,160 206,206 214,242 L192,242 C184,204 188,152 208,126 Z" fill="{NAVY2}"/>
<path d="M242,126 L234,130 C244,160 246,206 238,242 L250,242 C262,204 260,152 242,126 Z" fill="{NAVY}"/>
<rect x="216" y="104" width="18" height="28" rx="5" fill="{SKIN}"/>
{head(225,80,1.12)}
<!-- front leg: thigh out to the right, shin down -->
<path d="M232,236 L290,246 L296,330" stroke="{NAVY}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
<path d="M286,328 C278,332 272,340 278,346 L312,346 L308,326 Z" fill="{DARK}"/>
<!-- arms: hands resting on the front thigh -->
<path d="M200,142 C186,176 190,212 212,244" stroke="{NAVY}" stroke-width="17" stroke-linecap="round" fill="none"/>
<path d="M248,142 C262,176 258,212 250,244" stroke="{NAVY}" stroke-width="17" stroke-linecap="round" fill="none"/>
<ellipse cx="216" cy="250" rx="10" ry="8" fill="{SKIN}"/><ellipse cx="254" cy="250" rx="10" ry="8" fill="{SKIN}"/>
''')

open("images/illustrations/intro.svg","w").write(intro)
print("written")
