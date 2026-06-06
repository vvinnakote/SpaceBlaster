# ============================================================
#  CURVED PATHS — Make enemies fly in curves using polynomials!
# ============================================================
#
#  Hey Vivaan! This file controls HOW the enemy UFOs move.
#
#  Right now they fly straight down. Boring!
#  With polynomials, you can make them swoop, curve, and zigzag.
#
#
#  ╔═══════════════════════════════════════════════════════════╗
#  ║  LEARN MORE ABOUT POLYNOMIALS:                           ║
#  ║                                                          ║
#  ║  Khan Academy (great videos + practice):                 ║
#  ║    https://www.khanacademy.org/math/algebra/             ║
#  ║      x2f8bb11595b61c86:quadratics-multiplying-factoring  ║
#  ║                                                          ║
#  ║  Math is Fun (simple explanations + graphs):             ║
#  ║    https://www.mathsisfun.com/algebra/polynomials.html   ║
#  ║                                                          ║
#  ║  Desmos Graphing Calculator (type formulas, see curves): ║
#  ║    https://www.desmos.com/calculator                     ║
#  ║    → Try typing: y = 300x^2  or  y = 800x^3 - 600x^2   ║
#  ║    → x is like our "t" (0 to 1), y is the sideways move ║
#  ║                                                          ║
#  ║  GeoGebra (interactive math tool):                       ║
#  ║    https://www.geogebra.org/graphing                     ║
#  ╚═══════════════════════════════════════════════════════════╝
#
#
#  HOW IT WORKS IN THIS GAME:
#  ──────────────────────────
#  As an enemy flies from the top to the bottom of the screen,
#  we track its progress as a number "t" that goes from 0.0 to 1.0:
#
#      t = 0.0  →  enemy is at the TOP of the screen
#      t = 0.5  →  enemy is HALFWAY down
#      t = 1.0  →  enemy is at the BOTTOM
#
#  A "path function" takes t and returns how far LEFT or RIGHT
#  the enemy should move from where it started (in pixels).
#
#      positive number → move RIGHT
#      negative number → move LEFT
#      zero            → stay in the middle (straight down)
#
#  The screen is 800 pixels wide, so values between -380 and +380
#  will keep the enemy on screen.
#
#
#  WHAT IS A POLYNOMIAL?
#  ─────────────────────
#  A polynomial is just a math formula using powers of a variable:
#
#      f(t) = a * t  +  b * t²  +  c * t³
#
#  Each part is called a "term". Let's break it down:
#
#      a * t    → "linear" term (degree 1) — makes a straight diagonal line
#      b * t²   → "quadratic" term (degree 2) — makes a smooth curve (parabola)
#      c * t³   → "cubic" term (degree 3) — makes an S-shaped curve
#      d * t⁴   → "quartic" term (degree 4) — even curvier!
#      e * t⁵   → "quintic" term (degree 5) — wild wiggles!
#
#  The DEGREE of a polynomial = the highest power of t.
#      f(t) = 300 * t²              → degree 2 (quadratic)
#      f(t) = 800 * t³ - 600 * t²   → degree 3 (cubic)
#
#
#  WHAT DO THE NUMBERS (COEFFICIENTS) DO?
#  ──────────────────────────────────────
#  The number in front of each term controls the SIZE of the curve:
#
#      100 * t²   → small curve  (moves up to 100 pixels)
#      300 * t²   → medium curve (moves up to 300 pixels)
#      500 * t²   → big curve    (moves up to 500 pixels — almost off screen!)
#
#  A NEGATIVE number flips the direction:
#
#      300 * t²   → curves to the RIGHT
#     -300 * t²   → curves to the LEFT
#
#
#  COMBINING TERMS — WHERE THE MAGIC HAPPENS:
#  ──────────────────────────────────────────
#  When you add multiple terms together, they "fight" each other
#  and create interesting shapes!
#
#  Example: f(t) = 800 * t² - 800 * t³
#
#      At t = 0.0: both terms are 0, so offset = 0
#      At t = 0.5: 800*(0.25) - 800*(0.125) = 200 - 100 = 100   → moved RIGHT
#      At t = 1.0: 800*(1.0) - 800*(1.0) = 800 - 800 = 0        → back to CENTER!
#
#  This creates a "swoop" — goes right in the middle, comes back at the end!
#
#
#  QUICK RECIPE TABLE:
#  ──────────────────
#  Want this shape?          Use this polynomial:
#  ───────────────           ────────────────────
#  Straight diagonal         200 * t
#  Smooth curve right        300 * t ** 2
#  Smooth curve left        -300 * t ** 2
#  S-shape (left then right) 800 * t**3 - 600 * t**2
#  Swoop out and back        800 * t**2 - 800 * t**3
#  Sharp late curve           300 * t ** 3
#  Gentle then sudden         100 * t + 200 * t ** 3
#  Zigzag madness            2400*t**5 - 6000*t**4 + 4800*t**3 - 1200*t**2
#
# ============================================================


def straight_down(t):
    """
    The simplest path — no curve at all.
    The enemy just falls straight down.

    Polynomial: f(t) = 0     (degree 0 — just a constant!)

    No matter what t is, the answer is always 0.
    That means: no sideways movement at all.
    """
    return 0


def gentle_curve_right(t):
    """
    A curve to the right — this is a QUADRATIC (degree 2) polynomial.

    Polynomial: f(t) = 300 * t²

    Let's calculate some values:
      t = 0.0  →  300 * 0.0² = 0      pixels  (at the top — no movement)
      t = 0.25 →  300 * 0.0625 = 19   pixels  (barely moved)
      t = 0.5  →  300 * 0.25 = 75     pixels  (starting to curve)
      t = 0.75 →  300 * 0.5625 = 169  pixels  (curving fast now!)
      t = 1.0  →  300 * 1.0 = 300     pixels  (full curve at the bottom)

    Notice how it starts SLOW and gets FASTER? That's what t² does!
    This shape is called a PARABOLA.

    → Try on Desmos: type y = 300x^2 and look at the curve from x=0 to x=1

    EXPERIMENTS:
      Change 300 to 500  → sharper curve (moves further right)
      Change 300 to 100  → gentler curve (barely moves)
      Change 300 to -300 → curves LEFT instead of right
    """
    return 300 * t ** 2


def gentle_curve_left(t):
    """
    Same curve as gentle_curve_right, but NEGATIVE so it goes LEFT.

    Polynomial: f(t) = -300 * t²

    The only difference is the minus sign (-300 instead of 300).
    Negative = LEFT, Positive = RIGHT. That's all!
    """
    return -300 * t ** 2


def s_curve(t):
    """
    An S-shaped path — this is a CUBIC (degree 3) polynomial.

    Polynomial: f(t) = 800 * t³ - 600 * t²

    This has TWO terms that "fight" each other:
      -600 * t²  → pulls LEFT  (this one wins at the start)
       800 * t³  → pulls RIGHT (this one wins at the end)

    Let's calculate:
      t = 0.0  →  800*0    - 600*0     =  0     (center)
      t = 0.25 →  800*0.016 - 600*0.063 = 13 - 38 = -25   (going LEFT)
      t = 0.5  →  800*0.125 - 600*0.25  = 100 - 150 = -50  (still LEFT)
      t = 0.75 →  800*0.422 - 600*0.563 = 338 - 338 = 0    (back to CENTER!)
      t = 1.0  →  800*1.0   - 600*1.0   = 800 - 600 = 200  (now RIGHT!)

    See the S? LEFT → CENTER → RIGHT!

    → Try on Desmos: type y = 800x^3 - 600x^2

    EXPERIMENTS:
      Swap the signs: -800 * t³ + 600 * t²   → mirror S (RIGHT then LEFT)
      Make it wider:   1200 * t³ - 900 * t²   → bigger S shape
      Make it tighter:  400 * t³ - 300 * t²   → smaller S shape
    """
    return 800 * t ** 3 - 600 * t ** 2


def swoop(t):
    """
    Swoops to the RIGHT and then comes BACK to center.

    Polynomial: f(t) = 800 * t² - 800 * t³

    This is the OPPOSITE of s_curve. Both terms have the same
    coefficient (800) but different powers, so they cancel out
    perfectly at t=1.0!

    Let's calculate:
      t = 0.0  →  800*0    - 800*0     =  0    (center)
      t = 0.25 →  800*0.063 - 800*0.016 = 50 - 13 = 37   (going RIGHT)
      t = 0.5  →  800*0.25  - 800*0.125 = 200 - 100 = 100 (peak! furthest RIGHT)
      t = 0.75 →  800*0.563 - 800*0.422 = 450 - 338 = 112 (starting to come back)
      t = 1.0  →  800*1.0   - 800*1.0   = 800 - 800 = 0   (back to CENTER!)

    The enemy goes out to the side and returns. Sneaky!

    → Try on Desmos: type y = 800x^2 - 800x^3

    EXPERIMENTS:
      Bigger swoop:  1200 * t²  - 1200 * t³   → goes further out
      Left swoop:    -800 * t²  + 800 * t³     → swoops LEFT instead
      Lopsided:       800 * t²  - 600 * t³     → doesn't fully come back
    """
    return 800 * t ** 2 - 800 * t ** 3


def zigzag(t):
    """
    A wild zigzag path — this is a QUINTIC (degree 5) polynomial!

    Polynomial: f(t) = 2400 * t⁵ - 6000 * t⁴ + 4800 * t³ - 1200 * t²

    This has FOUR terms fighting each other, creating multiple
    direction changes — the enemy goes LEFT, then RIGHT, then LEFT again!

    The higher the degree, the more "wiggles" you can create.
    Degree 2 = 0 wiggles (smooth curve)
    Degree 3 = 1 wiggle  (S-shape)
    Degree 5 = 2 wiggles (zigzag!)

    This is the hardest path to dodge because the enemy keeps
    changing direction unexpectedly.

    → Try on Desmos: type y = 2400x^5 - 6000x^4 + 4800x^3 - 1200x^2

    EXPERIMENTS:
      Double everything for EXTREME zigzag:
        4800*t**5 - 12000*t**4 + 9600*t**3 - 2400*t**2
      Flip it (mirror image):
        -2400*t**5 + 6000*t**4 - 4800*t**3 + 1200*t**2
    
    WARNING: This one is tricky to dodge!
    """
    return 2400 * t**5 - 6000 * t**4 + 4800 * t**3 - 1200 * t**2


# ============================================================
#  YOUR CUSTOM PATH — Edit this one!
# ============================================================

def my_custom_path(t):
    """
    ★ THIS IS YOUR PATH, VIVAAN! EDIT THIS ONE! ★

    Edit the return line below to create your own curve.
    Start simple, then make it crazier!

    Current polynomial: f(t) = 200 * t²

    ──────────────────────────────────────────────────────────
    STEP-BY-STEP: How to design your own path
    ──────────────────────────────────────────────────────────

    1. Pick a shape from the recipe table at the top of this file
    2. Copy it into the return line below
    3. Run the game and see what happens!
    4. Change the numbers to adjust the curve
    5. Add more terms to make it crazier

    EXAMPLE IDEAS TO TRY (copy one into the return line):

      return 100 * t                          # diagonal line (degree 1)
      return 300 * t ** 2                      # smooth curve right (degree 2)
      return -300 * t ** 2                     # smooth curve left
      return 300 * t ** 3                      # late sharp curve (degree 3)
      return 800 * t ** 2 - 800 * t ** 3       # swoop out and back
      return 800 * t ** 3 - 600 * t ** 2       # S-shape
      return 100 * t + 200 * t ** 3            # diagonal + late curve
      return -200 * t ** 2 + 400 * t ** 3      # left then right
      return 300 * t ** 2 - 100 * t            # starts left, curves right

    CHALLENGE IDEAS:
      → Can you make a path that goes RIGHT, then LEFT, then RIGHT?
        (Hint: you'll need t², t³, AND t⁴ terms!)
      → Can you make a path that barely moves until the very end?
        (Hint: use a high power like t⁵ with a big number)
      → Can you make a path that starts fast and slows down?
        (Hint: try a linear term minus a squared term: 300*t - 300*t**2)

    → Open https://www.desmos.com/calculator and type your formula
      to SEE the curve before running the game!
    """
    return 200 * t ** 2


# ============================================================
#  PATH LIST — Pick which paths the enemies will use
# ============================================================
#
#  Each enemy randomly picks one of these paths.
#  Add or remove paths to change the game!
#
#  To make ALL enemies use YOUR path, change it to:
#      paths = [my_custom_path]
#
#  To make the game harder, add more tricky paths:
#      paths = [s_curve, zigzag, swoop]
#

paths = [
    straight_down,
    gentle_curve_right,
    gentle_curve_left,
    s_curve,
    swoop,
    # my_custom_path,       # ← Remove the # to enable your path!
    # zigzag,               # ← Remove the # for zigzag (hard mode!)
]

# ============================================================
#  PATH CHOICES — used by the menu in the game
# ============================================================
#  The number the player types maps to a list of paths.
#  1 = Straight, 2 = Curves, 3 = S-Curve, 4 = Swoop, 5 = Zigzag, 6 = Mix all!

path_choices = {
    1: [straight_down],                                          # just straight down
    2: [gentle_curve_right, gentle_curve_left],                   # curving left or right
    3: [s_curve],                                                 # S-shaped paths
    4: [swoop],                                                   # swoop out and back
    5: [zigzag],                                                  # wild zigzag
    6: [gentle_curve_right, gentle_curve_left, s_curve, swoop, zigzag],  # mix of everything!
}
