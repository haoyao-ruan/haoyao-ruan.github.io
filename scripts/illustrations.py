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

# ---------- intro: sitting on a wooden desk, monitor and plants ----------
WOOD="#c9a078"; WOODL="#dcb98f"; WOODD="#a97c54"; POT="#e07a5f"; LEAF="#3fa66b"; LEAFD="#2d7a4f"; LEAFL="#6cc48f"
intro = svg(520,360,f'''
<!-- floor plant, left -->
<path d="M96,232 C70,200 66,160 92,140 C104,170 102,204 96,232 Z" fill="{LEAF}"/>
<path d="M96,232 C116,200 130,176 142,170 C136,206 118,226 96,232 Z" fill="{LEAFD}"/>
<path d="M96,232 C76,212 60,196 58,182 C78,190 92,208 96,232 Z" fill="{LEAFL}"/>
<path d="M96,232 C100,196 112,176 120,160 C122,196 110,220 96,232 Z" fill="{LEAFD}" opacity="0.8"/>
<path d="M70,230 L122,230 L114,300 L78,300 Z" fill="{POT}"/><rect x="66" y="226" width="60" height="10" rx="3" fill="#c9644c"/>
<!-- desk: wood top -->
<rect x="150" y="232" width="340" height="14" rx="3" fill="{WOOD}"/>
<rect x="150" y="232" width="340" height="4" rx="2" fill="{WOODL}"/>
<path d="M180,240 L260,240 M300,240 L360,240 M400,240 L470,240" stroke="{WOODD}" stroke-width="1.2" opacity="0.6"/>
<rect x="420" y="246" width="70" height="114" fill="{WOOD}"/>
<rect x="420" y="246" width="70" height="114" fill="none" stroke="{WOODD}" stroke-width="2"/>
<line x1="420" y1="284" x2="490" y2="284" stroke="{WOODD}" stroke-width="2"/><line x1="420" y1="322" x2="490" y2="322" stroke="{WOODD}" stroke-width="2"/>
<rect x="444" y="263" width="22" height="5" rx="2" fill="{WOODD}"/><rect x="444" y="301" width="22" height="5" rx="2" fill="{WOODD}"/><rect x="444" y="339" width="22" height="5" rx="2" fill="{WOODD}"/>
<rect x="150" y="246" width="12" height="114" fill="{WOOD}"/><rect x="150" y="246" width="12" height="114" fill="none" stroke="{WOODD}" stroke-width="2"/>
<!-- monitor with a chart -->
<rect x="318" y="118" width="124" height="86" rx="6" fill="{NAVY}"/>
<rect x="324" y="124" width="112" height="70" rx="3" fill="{WHITE}"/>
<path d="M334,184 L334,134 M334,184 L428,184" stroke="{GREY2}" stroke-width="2"/>
<path d="M338,182 C356,180 364,160 374,142 C384,124 392,124 400,142 C410,162 418,180 426,182" stroke="{ACC}" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M338,182 C356,180 364,160 374,142 C384,124 392,124 400,142 C410,162 418,180 426,182 Z" fill="{ACCL}" opacity="0.5"/>
<rect x="372" y="204" width="16" height="18" fill="{NAVY}"/><rect x="352" y="220" width="56" height="8" rx="3" fill="{NAVY}"/>
<!-- small plant on desk -->
<rect x="286" y="212" width="22" height="20" rx="3" fill="{POT}"/>
<path d="M297,212 C290,200 288,190 296,184 C300,194 299,204 297,212 Z" fill="{LEAF}"/>
<path d="M297,212 C304,202 310,196 314,194 C312,204 306,210 297,212 Z" fill="{LEAFD}"/>
<path d="M297,212 C290,206 284,200 282,196 C290,198 295,204 297,212 Z" fill="{LEAFL}"/>
<!-- figure: one continuous navy body -->
<g fill="{NAVY}" stroke="{NAVY}" stroke-linecap="round" stroke-linejoin="round">
  <path d="M208,120 C196,122 188,138 188,158 L186,252 L254,252 L252,158 C252,138 244,122 232,120 Z" stroke="none"/>
  <ellipse cx="220" cy="252" rx="36" ry="16" stroke="none"/>
  <path d="M210,252 L203,340" stroke-width="26" fill="none"/>
  <path d="M232,250 L288,254 L296,332" stroke-width="26" fill="none"/>
</g>
<!-- shoes -->
<path d="M194,338 C184,342 176,350 182,356 L216,356 L216,338 Z" fill="{DARK}"/>
<path d="M286,330 C276,334 270,342 276,348 L312,348 L310,328 Z" fill="{DARK}"/>
<!-- jacket opening with accent top -->
<path d="M212,120 C214,160 212,210 214,252 L228,252 C230,210 228,160 230,120 Z" fill="{ACC}"/>
<path d="M208,120 L216,120 C210,160 208,212 216,252 L188,252 L188,158 C188,138 196,122 208,120 Z" fill="{NAVY2}"/>
<!-- neck and collar -->
<rect x="213" y="98" width="16" height="30" rx="5" fill="{SKIN}"/>
<path d="M206,124 L214,110 L222,128 Z" fill="{NAVY2}"/><path d="M234,124 L228,110 L220,128 Z" fill="{NAVY}"/>
{head(221,80,1.12)}
<!-- arms resting on the front thigh -->
<path d="M199,142 C186,176 190,212 210,248" stroke="{NAVY2}" stroke-width="17" stroke-linecap="round" fill="none"/>
<path d="M243,142 C258,176 256,212 250,248" stroke="{NAVY}" stroke-width="17" stroke-linecap="round" fill="none"/>
<ellipse cx="215" cy="254" rx="10" ry="8" fill="{SKIN}"/><ellipse cx="253" cy="254" rx="10" ry="8" fill="{SKIN}"/>
''')

open("images/illustrations/intro.svg","w").write(intro)
print("written")
