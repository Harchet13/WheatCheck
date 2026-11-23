"""A looping, CSS-only animation that shows how to use WheatCheck in four steps."""
from html import escape

# Each of the four scenes is on screen for a quarter of the loop.
LOOP_SECONDS = 16

_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: #fff;
       display: flex; flex-direction: column; align-items: center; background: transparent; }
.phone { position: relative; width: 220px; height: 380px; border-radius: 30px;
         border: 8px solid #1d1f27; background: #f4f1e8; overflow: hidden;
         box-shadow: 0 10px 30px rgba(0,0,0,.35); }
.phone::before { content: ""; position: absolute; top: 6px; left: 50%; width: 60px; height: 6px;
                 margin-left: -30px; border-radius: 3px; background: #1d1f27; z-index: 9; }
.scene, .caption { position: absolute; inset: 0; opacity: 0;
                   animation: show var(--loop) infinite; animation-delay: var(--at); }
.s1 { --at: 0s; } .s2 { --at: calc(var(--loop) / 4); }
.s3 { --at: calc(var(--loop) / 2); } .s4 { --at: calc(var(--loop) * 3 / 4); }
@keyframes show { 0% { opacity: 0; } 2%, 23% { opacity: 1; } 25%, 100% { opacity: 0; } }

/* Scene 1: take the photo */
.field { position: absolute; inset: 0; background: linear-gradient(#8fc6e8 0 35%, #c9a84a 35% 100%); }
.leaf { position: absolute; left: 50%; top: 110px; width: 70px; height: 190px; margin-left: -35px;
        background: #5f9e3b; border-radius: 50% 50% 50% 50% / 90% 90% 10% 10%; transform: rotate(-8deg); }
.spot { position: absolute; width: 9px; height: 5px; border-radius: 3px; background: #e2a412; }
.frame { position: absolute; inset: 70px 30px 90px; border: 3px dashed rgba(255,255,255,.9);
         border-radius: 10px; animation: zoom var(--loop) infinite; animation-delay: var(--at); }
@keyframes zoom { 0% { transform: scale(1.25); } 10%, 100% { transform: scale(1); } }
.shutter { position: absolute; bottom: 22px; left: 50%; width: 52px; height: 52px; margin-left: -26px;
           border-radius: 50%; background: #fff; border: 5px solid #d9d9d9;
           animation: press var(--loop) infinite; animation-delay: var(--at); }
@keyframes press { 0%, 12% { transform: scale(1); } 13% { transform: scale(.8); } 15%, 100% { transform: scale(1); } }
.flash { position: absolute; inset: 0; background: #fff; opacity: 0;
         animation: flash var(--loop) infinite; animation-delay: var(--at); }
@keyframes flash { 0%, 13% { opacity: 0; } 14% { opacity: .95; } 18%, 100% { opacity: 0; } }

/* Scene 2: upload it */
.drop { position: absolute; left: 22px; right: 22px; top: 150px; height: 130px; border-radius: 14px;
        border: 3px dashed #4b7c8a; background: #e6eef0; }
.arrow { position: absolute; left: 50%; bottom: 14px; margin-left: -14px; font-size: 28px; color: #4b7c8a; }
.thumb { position: absolute; left: 50%; width: 76px; height: 76px; margin-left: -38px; border-radius: 10px;
         background: linear-gradient(135deg, #5f9e3b 0 60%, #c9a84a 60%); border: 3px solid #fff;
         box-shadow: 0 4px 10px rgba(0,0,0,.3); animation: drop var(--loop) infinite; animation-delay: var(--at); }
@keyframes drop { 0%, 3% { top: 30px; } 12%, 100% { top: 172px; } }
.bar { position: absolute; left: 30px; right: 30px; top: 300px; height: 10px; border-radius: 5px; background: #d6d6d6; overflow: hidden; }
.bar i { display: block; height: 100%; width: 0; background: #2e9e5b;
         animation: fill var(--loop) infinite; animation-delay: var(--at); }
@keyframes fill { 0%, 12% { width: 0; } 21%, 100% { width: 100%; } }

/* Scene 3: tap Analyze */
.photo { position: absolute; left: 22px; right: 22px; top: 40px; height: 180px; border-radius: 12px; overflow: hidden;
         background: linear-gradient(135deg, #5f9e3b 0 60%, #c9a84a 60%); }
.scan { position: absolute; left: 0; right: 0; height: 4px; background: #ffe066; box-shadow: 0 0 12px #ffe066;
        animation: scan var(--loop) infinite; animation-delay: var(--at); }
@keyframes scan { 0%, 10% { top: -4px; opacity: 0; } 11% { opacity: 1; } 22% { top: 176px; opacity: 1; } 23%, 100% { opacity: 0; } }
.go { position: absolute; left: 30px; right: 30px; top: 250px; height: 50px; border-radius: 12px;
      background: #F5C518; color: #1b1b1b; font-weight: 700; font-size: 17px;
      display: flex; align-items: center; justify-content: center;
      animation: tap var(--loop) infinite; animation-delay: var(--at); }
@keyframes tap { 0%, 8% { transform: scale(1); } 9% { transform: scale(.92); filter: brightness(.85); } 11%, 100% { transform: scale(1); } }
.finger { position: absolute; font-size: 38px; animation: finger var(--loop) infinite; animation-delay: var(--at); }
@keyframes finger { 0% { top: 360px; left: 150px; } 8%, 10% { top: 270px; left: 110px; } 16%, 100% { top: 360px; left: 150px; } }

/* Scene 4: read the result and buy the remedy */
.card { position: absolute; left: 16px; right: 16px; top: 34px; padding: 14px; border-radius: 14px;
        background: #fff; color: #222; box-shadow: 0 4px 12px rgba(0,0,0,.15); }
.card b { display: block; font-size: 18px; color: #a33b12; margin-bottom: 8px; }
.conf { height: 9px; border-radius: 5px; background: #e4e4e4; overflow: hidden; margin-bottom: 12px; }
.conf i { display: block; height: 100%; width: 0; background: #2e9e5b;
          animation: conf var(--loop) infinite; animation-delay: var(--at); }
@keyframes conf { 0%, 2% { width: 0; } 10%, 100% { width: 92%; } }
.line { height: 8px; border-radius: 4px; background: #e8e8e8; margin: 8px 0; }
.buy { position: absolute; left: 30px; right: 30px; top: 250px; height: 50px; border-radius: 25px;
       background: #2e9e5b; color: #fff; font-weight: 700; font-size: 16px;
       display: flex; align-items: center; justify-content: center;
       animation: pulse 1.2s ease-in-out infinite; }
@keyframes pulse { 50% { transform: scale(1.06); } }

/* Caption and progress dots */
.captions { position: relative; width: 100%; max-width: 420px; height: 64px; margin-top: 14px; }
.caption { display: flex; align-items: center; justify-content: center; gap: 10px;
           font-size: 18px; font-weight: 600; text-align: center; line-height: 1.3; }
.num { flex: none; width: 32px; height: 32px; border-radius: 50%; background: #F5C518; color: #1b1b1b;
       display: flex; align-items: center; justify-content: center; font-weight: 800; }
.dots { display: flex; gap: 8px; margin-top: 4px; }
.dot { width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,.35); position: relative; }
.dot::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: #F5C518; opacity: 0;
              animation: show var(--loop) infinite; animation-delay: var(--at); }
@media (prefers-reduced-motion: reduce) {
  .frame, .shutter, .flash, .thumb, .bar i, .scan, .go, .finger, .conf i, .buy { animation: none; }
  .thumb { top: 172px; } .bar i { width: 100%; } .conf i { width: 92%; } .finger { display: none; }
}
"""


def howto_html(captions, analyze_label, example_disease, buy_label):
    """HTML for the animation, with on-screen text in the user's language.

    captions: one caption per step (four). analyze_label: text of the Analyze
    button. example_disease: disease name shown on the result card.
    buy_label: text of the buy button on the result card.
    """
    assert len(captions) == 4, captions
    captions = [escape(c) for c in captions]
    spots = "".join(
        f'<span class="spot" style="left:{x}px;top:{y}px"></span>'
        for x, y in [(18, 40), (40, 62), (24, 90), (44, 118), (20, 140), (36, 30)]
    )
    caption_html = "".join(
        f'<div class="caption s{i}"><span class="num">{i}</span><span>{c}</span></div>'
        for i, c in enumerate(captions, 1)
    )
    dots = "".join(f'<span class="dot s{i}"></span>' for i in range(1, 5))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
:root {{ --loop: {LOOP_SECONDS}s; }}
{_CSS}</style></head><body>
<div class="phone">
  <div class="scene s1"><div class="field"></div><div class="leaf">{spots}</div>
    <div class="frame"></div><div class="shutter"></div><div class="flash"></div></div>
  <div class="scene s2"><div class="drop"><span class="arrow">⬆</span></div><div class="thumb"></div>
    <div class="bar"><i></i></div></div>
  <div class="scene s3"><div class="photo"><div class="scan"></div></div>
    <div class="go">{escape(analyze_label)}</div><div class="finger">👆</div></div>
  <div class="scene s4"><div class="card"><b>{escape(example_disease)}</b><div class="conf"><i></i></div>
    <div class="line"></div><div class="line" style="width:80%"></div><div class="line" style="width:60%"></div></div>
    <div class="buy">{escape(buy_label)}</div></div>
</div>
<div class="captions">{caption_html}</div>
<div class="dots">{dots}</div>
</body></html>"""
