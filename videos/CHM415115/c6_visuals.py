"""Draw functions for CHM415115 Criterion 6 (thermochemistry, kinetics and equilibrium).  draw(fig, s, ph): s = step, ph = phase."""
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Polygon

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, eq, chip, wax, gax, darrow, arrow, label, frac,
                              FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK, GREEN, YELLOW, TAU)
from explainer.spec import import_sibling

_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, C, ch, fit = _CC.Slide, _CC.Seq, _CC.C, _CC.ch, _CC.fit


# ============================================================================ energy profile
def _profile(x, R, P, H, x0=45.0, w=11.0):
    """Smooth reaction profile: reactants at R, products at P, a peak H above the higher of them near x0."""
    t = np.clip((x - 30) / 30.0, 0, 1)
    base = R + (P - R) * (t * t * (3 - 2 * t))
    return base + H * np.exp(-((x - x0) / w) ** 2)


def energy_axes(fig, rect, ylim=(0, 100)):
    ax = gax(fig, rect, (0, 100), ylim, 'Reaction coordinate', 'Enthalpy (kJ mol⁻¹)', ticks=False)
    return ax


def pe_diagram(ax, kind='exo', cat=False, labels=True, both_ea=False, reac='reactants', prod='products', show_h=True,
               show_ea=True, R0=None):
    C1, C2 = C()
    x = np.linspace(0, 100, 400)
    if kind == 'exo':
        R, P, H = 62, 28, 24
    else:
        R, P, H = 30, 58, 30
    peak = max(R, P) + H
    ax.plot(x, _profile(x, R, P, H), color=C1, lw=4, zorder=3)
    ax.hlines(R, 0, 30, color=SOFT, lw=1.5, ls=':')
    ax.hlines(P, 62, 100, color=SOFT, lw=1.5, ls=':')
    if labels:
        ax.text(3, R + 6, reac, color=FG, fontsize=19, weight='bold', ha='left')
        ax.text(97, P + 6, prod, color=FG, fontsize=19, weight='bold', ha='right')
    if show_ea:
        ax.annotate('', (20, peak - 3), (20, R), arrowprops=dict(arrowstyle='<|-|>', color=YELLOW, lw=2.8))
        ax.text(23, (R + peak) / 2, 'Ea', color=YELLOW, fontsize=22, weight='bold', va='center')
    if both_ea:
        ax.annotate('', (80, peak - 3), (80, P), arrowprops=dict(arrowstyle='<|-|>', color=PINK, lw=2.8))
        ax.text(83, (P + peak) / 2, 'Ea (reverse)', color=PINK, fontsize=19, weight='bold', va='center')
    if show_h:
        ax.annotate('', (70, P), (70, R), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=3.2))
        ax.text(72, (R + P) / 2, 'ΔH ' + ('< 0' if kind == 'exo' else '> 0'), color=GREEN, fontsize=22, weight='bold', va='center')
    if cat:
        pk = max(R, P) + H * 0.45
        ax.plot(x, _profile(x, R, P, H * 0.45), color=PINK, lw=3.5, ls='--', zorder=2)
        ax.text(50, pk + 3, 'catalysed', color=PINK, fontsize=18, ha='center')
        ax.text(45, peak + 2, 'uncatalysed', color=C1, fontsize=18, ha='center')
    ax.set_ylim(0, 100)


def pe_exo(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Energy profile: an exothermic reaction')
    chip(fig, 'Element 2 · energy diagrams')
    ax = energy_axes(fig, [0.06, 0.12, 0.55, 0.66])
    pe_diagram(ax, 'exo', reac='CH₄(g) + 2O₂(g)', prod='CO₂(g) + 2H₂O(l)', show_h=s >= 1, show_ea=s >= 0)
    notes = ['Reactants start at a stated level. Break bonds first: energy goes UP by Ea to the peak',
             'Forming new bonds releases more energy than was absorbed, so the products end LOWER: ΔH is negative',
             'Label: species with states, coefficients, Ea and ΔH with arrows. Do not start at ΔH = 0']
    y = 0.78
    for i in range(min(3, s + 1)):
        t = fit(ch(notes[i]), 0.30, 21)
        T(fig, 0.64, y, t, size=21, color=FG if i == min(s, 2) else SOFT)
        y -= frac(21) * (t.count('\n') + 1) + 0.03


def pe_endo(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Energy profile: an endothermic reaction')
    chip(fig, 'Element 2 · energy diagrams')
    ax = energy_axes(fig, [0.06, 0.12, 0.55, 0.66])
    pe_diagram(ax, 'endo', reac='NH₄Cl(s)', prod='NH₃(g) + HCl(g)', show_h=True)
    notes = ['Products end HIGHER than reactants: more energy absorbed breaking bonds than released making them. ΔH is positive',
             'Endothermic changes cool their surroundings: dissolving calcium chloride cools the water, dissolving potassium hydroxide warms it',
             'Bond breaking ALWAYS absorbs energy. “Breaking the bond releases energy” is a false statement, even for ATP']
    y = 0.78
    for i in range(min(3, s + 1)):
        t = fit(ch(notes[i]), 0.30, 21)
        T(fig, 0.64, y, t, size=21, color=FG if i == min(s, 2) else SOFT)
        y -= frac(21) * (t.count('\n') + 1) + 0.03


def pe_cat(fig, s, ph):
    C1, C2 = C()
    header(fig, 'A catalyst: a new pathway')
    chip(fig, 'Element 3 · rates and catalysis')
    ax = energy_axes(fig, [0.06, 0.12, 0.55, 0.66])
    pe_diagram(ax, 'exo', cat=s >= 0, reac='SO₂ + ½O₂', prod='SO₃', show_h=True, both_ea=s >= 2)
    notes = ['A catalyst provides an alternative pathway with a LOWER activation energy',
             'ΔH is unchanged: it depends only on reactants and products (Hess’s law), not the pathway',
             'It lowers Ea for the forward AND the reverse reaction, so it changes the rate but not the position of equilibrium',
             'It is not consumed. An enzyme is a biological catalyst']
    y = 0.78
    for i in range(min(4, s + 1)):
        t = fit(ch(notes[i]), 0.30, 21)
        T(fig, 0.64, y, t, size=21, color=FG if i == min(s, 3) else SOFT)
        y -= frac(21) * (t.count('\n') + 1) + 0.03


def pe_reverse(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Why reactions are reversible')
    chip(fig, 'Element 4 · equilibrium')
    ax = energy_axes(fig, [0.06, 0.12, 0.55, 0.66])
    pe_diagram(ax, 'exo', both_ea=True, reac='reactants', prod='products')
    notes = ['Both directions need to climb a barrier: forward Ea, reverse Ea',
             'For an exothermic reaction the reverse barrier is bigger: Ea(reverse) = Ea(forward) + |ΔH|',
             'Raise the temperature: both rates rise, but the reaction with the LARGER Ea (the reverse, endothermic one) gains more, so the equilibrium shifts that way']
    y = 0.78
    for i in range(min(3, s + 1)):
        t = fit(ch(notes[i]), 0.30, 21)
        T(fig, 0.64, y, t, size=21, color=FG if i == min(s, 2) else SOFT)
        y -= frac(21) * (t.count('\n') + 1) + 0.03


# ============================================================================ distribution of energies
def mbd(E, kT):
    f = np.sqrt(E) * np.exp(-E / kT)
    return f / np.trapezoid(f, E) if hasattr(np, 'trapezoid') else f / np.trapz(f, E)


def distribution(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Distribution of molecular energies')
    chip(fig, 'Element 3 · rates and catalysis')
    ax = gax(fig, [0.07, 0.14, 0.55, 0.64], (0, 8), (0, 0.62), 'Kinetic energy of a molecule', 'Number of molecules', ticks=False)
    E = np.linspace(0, 8, 600)
    Ea = 3.6
    low = mbd(E, 1.0)
    ax.plot(E, low, color=C1, lw=4)
    ax.axvline(Ea, color=YELLOW, lw=2.5, ls='--')
    ax.text(Ea + 0.08, 0.57, 'Ea', color=YELLOW, fontsize=22, weight='bold')
    ax.fill_between(E, 0, low, where=E >= Ea, color=C1, alpha=0.45)
    ax.text(0.9, 0.52, 'lower T', color=C1, fontsize=19, weight='bold')
    if s >= 1:
        hi = mbd(E, 1.6)
        ax.plot(E, hi, color=PINK, lw=4)
        ax.fill_between(E, 0, hi, where=E >= Ea, color=PINK, alpha=0.4)
        ax.text(3.0, 0.20, 'higher T', color=PINK, fontsize=19, weight='bold')
    if s >= 2:
        ax.axvline(2.3, color=GREEN, lw=2.5, ls='--')
        ax.text(2.35, 0.57, 'Ea with a catalyst', color=GREEN, fontsize=19, weight='bold')
        ax.fill_between(E, 0, low, where=E >= 2.3, color=GREEN, alpha=0.25)
    notes = ['Molecules have a spread of kinetic energies, not one value. Only those with energy at least Ea (shaded) can react',
             'Raising T: the peak lowers and moves right, the area under the curve stays the same, and a much larger share of molecules is above Ea. So a small rise in T gives a large rise in rate',
             'A catalyst does not change the curve. It lowers Ea, so more molecules are above it. Collision frequency is the same, but more collisions are effective']
    y = 0.78
    for i in range(min(3, s + 1)):
        t = fit(ch(notes[i]), 0.30, 20)
        T(fig, 0.65, y, t, size=20, color=FG if i == min(s, 2) else SOFT)
        y -= frac(20) * (t.count('\n') + 1) + 0.028


# ============================================================================ rate graphs
V_INF, TAU_S = 120.0, 25.0   # mL and s for the worked example's curve


def vol(t, vinf=V_INF, tau=TAU_S):
    return vinf * (1 - np.exp(-np.asarray(t) / tau))


def rate_graph(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Reading rates from a graph')
    chip(fig, 'Element 5 · calculations')
    ax = gax(fig, [0.07, 0.14, 0.52, 0.64], (0, 100), (0, 130), 'Time (s)', 'Volume of gas (mL)')
    t = np.linspace(0, 100, 300)
    ax.plot(t, vol(t), color=C1, lw=4)
    ax.set_yticks([0, 40, 80, 120]); ax.set_xticks([0, 20, 40, 60, 80, 100])
    if s >= 0:
        ax.plot([0, 40], [0, float(vol(40))], color=YELLOW, lw=2.5, ls='--')
        ax.scatter([0, 40], [0, float(vol(40))], color=YELLOW, zorder=5)
        ax.text(42, float(vol(40)) - 8, 'average: slope of the chord', color=YELLOW, fontsize=17)
    if s >= 1:
        t0 = 20.0; v0 = float(vol(t0)); m = V_INF / TAU_S * np.exp(-t0 / TAU_S)
        tt = np.array([0, 55.0])
        ax.plot(tt, v0 + m * (tt - t0), color=PINK, lw=2.8)
        ax.scatter([t0], [v0], color=PINK, zorder=6)
        ax.text(58, v0 + m * (55 - t0) - 6, 'instantaneous at 20 s:\nslope of the tangent', color=PINK, fontsize=17)
    if s >= 2:
        ax.axhline(V_INF, color=GREEN, lw=2, ls=':')
        ax.text(60, V_INF + 3, 'flat: a reactant is used up', color=GREEN, fontsize=17)
    notes = [ch('Average rate = change / time. In moles: Δn / t. In concentration: Δc / t. From gas volume: V / molar volume first'),
             'Rate at one moment: draw a tangent, and use its gradient. The slope is steepest at the start',
             'The curve flattens when the limiting reagent is used up, not because equilibrium is reached. The instantaneous rate is then zero']
    y = 0.78
    for i in range(min(3, s + 1)):
        t_ = fit(notes[i], 0.32, 20)
        T(fig, 0.62, y, t_, size=20, color=FG if i == min(s, 2) else SOFT)
        y -= frac(20) * (t_.count('\n') + 1) + 0.03


def rate_sketch(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Sketching a changed rate')
    chip(fig, 'Element 3 · rates and catalysis')
    ax = gax(fig, [0.07, 0.14, 0.52, 0.64], (0, 100), (0, 130), 'Time (s)', 'Volume of gas (mL)', ticks=False)
    t = np.linspace(0, 100, 300)
    ax.plot(t, vol(t), color=C1, lw=4); ax.text(70, 100, 'original', color=C1, fontsize=18)
    if s == 0:
        ax.plot(t, vol(t, tau=12.0), color=PINK, lw=4); ax.text(14, 118, 'faster, same final volume', color=PINK, fontsize=18)
    if s == 1:
        ax.plot(t, vol(t, vinf=60.0), color=GREEN, lw=4); ax.text(40, 66, 'half the limiting reagent:\nsame start slope, half the volume', color=GREEN, fontsize=18)
    if s >= 2:
        ax.plot(t, vol(t, vinf=60.0, tau=12.0), color=YELLOW, lw=4)
        ax.text(30, 66, 'smaller pieces AND half the amount:\nsteeper start, plateau at half', color=YELLOW, fontsize=18)
    notes = ['More concentrated acid, smaller pieces, or higher T: the slope at the start is steeper and the plateau arrives sooner. The final volume is the same, because the same amount of limiting reagent is used',
             'Less limiting reagent: the initial slope is the same (same concentrations), but the plateau is lower',
             'Draw on the graph you were given, from the same start. Show the new plateau at the right height, and the steeper slope']
    y = 0.78
    for i in range(min(3, s + 1)):
        t_ = fit(ch(notes[i]), 0.32, 20)
        T(fig, 0.62, y, t_, size=20, color=FG if i == min(s, 2) else SOFT)
        y -= frac(20) * (t_.count('\n') + 1) + 0.03


# ============================================================================ equilibrium graphs
def eq_dynamic(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Dynamic equilibrium')
    chip(fig, 'Element 4 · equilibrium')
    t = np.linspace(0, 10, 300)
    k = np.exp(-t / 1.6)
    ax = gax(fig, [0.06, 0.15, 0.40, 0.60], (0, 10), (0, 1.05), 'Time', 'Concentration', ticks=False)
    A = 0.35 + 0.65 * k
    ax.plot(t, A, color=C1, lw=4); ax.plot(t, 1 - A, color=PINK, lw=4)
    ax.text(0.4, 0.93, 'reactant', color=C1, fontsize=18); ax.text(0.4, 0.05, 'product', color=PINK, fontsize=18)
    ax2 = gax(fig, [0.55, 0.15, 0.40, 0.60], (0, 10), (0, 1.05), 'Time', 'Rate', ticks=False)
    fwd = 0.5 + 0.4 * k
    rev = 0.5 * (1 - k)
    ax2.plot(t, fwd, color=C1, lw=4); ax2.plot(t, rev, color=PINK, lw=4)
    ax2.text(0.4, 0.93, 'forward rate', color=C1, fontsize=18); ax2.text(5.5, 0.18, 'reverse rate', color=PINK, fontsize=18)
    if s >= 1:
        ax.axvline(5.0, color=YELLOW, lw=2, ls=':'); ax.text(5.1, 0.5, 'equilibrium', color=YELLOW, fontsize=18)
        ax2.axvline(5.0, color=YELLOW, lw=2, ls=':')
        ax2.text(5.6, 0.62, 'equal, NOT zero', color=YELLOW, fontsize=18, weight='bold')
    notes = ['In a closed system a reversible reaction stops changing: the concentrations level off',
             'At equilibrium, both reactions are still happening. The forward and reverse rates are equal, not zero']
    for i in range(min(2, s + 1)):
        T(fig, 0.06 + i * 0.49, 0.82, fit(notes[i], 0.40, 20), size=20, color=FG if i == min(s, 1) else SOFT)


def eq_disturb(fig, s, ph):
    """2SO2 + O2 <=> 2SO3: before 1.6 / 1.2 / 0.8; O2 added at A (+0.8); shift x = 0.3 by B; flat to C."""
    C1, C2 = C()
    header(fig, 'Adding a reactant to an equilibrium')
    chip(fig, 'Element 4 · equilibrium')
    ax = gax(fig, [0.07, 0.14, 0.52, 0.64], (0, 30), (0, 2.5), 'Time (min)', 'Concentration (mol L⁻¹)', ticks=False)
    A, B = 10.0, 20.0
    x0 = 0.3
    t1 = np.linspace(0, A, 20)
    ax.plot(t1, np.full_like(t1, 1.2), color=C1, lw=4)
    ax.plot(t1, np.full_like(t1, 1.6), color=YELLOW, lw=4)
    ax.plot(t1, np.full_like(t1, 0.8), color=PINK, lw=4)
    ax.axvline(A, color=MUT, lw=1.5, ls=':'); ax.text(A, 2.38, 'A', color=SOFT, fontsize=18, ha='center')
    ax.text(1, 1.27, 'O₂', color=C1, fontsize=18); ax.text(1, 1.67, 'SO₂', color=YELLOW, fontsize=18); ax.text(1, 0.87, 'SO₃', color=PINK, fontsize=18)
    if s >= 1:
        t2 = np.linspace(A, B, 100)
        k = 1 - np.exp(-(t2 - A) / 2.2)
        k = k / k[-1]
        ax.plot([A, A], [1.2, 2.0], color=C1, lw=4)
        ax.plot(t2, 2.0 - x0 * k, color=C1, lw=4)
        ax.plot(t2, 1.6 - 2 * x0 * k, color=YELLOW, lw=4)
        ax.plot(t2, 0.8 + 2 * x0 * k, color=PINK, lw=4)
        ax.axvline(B, color=MUT, lw=1.5, ls=':'); ax.text(B, 2.38, 'B', color=SOFT, fontsize=18, ha='center')
    if s >= 2:
        t3 = np.linspace(B, 30, 20)
        ax.plot(t3, np.full_like(t3, 2.0 - x0), color=C1, lw=4)
        ax.plot(t3, np.full_like(t3, 1.6 - 2 * x0), color=YELLOW, lw=4)
        ax.plot(t3, np.full_like(t3, 0.8 + 2 * x0), color=PINK, lw=4)
        ax.text(30, 2.38, 'C', color=SOFT, fontsize=18, ha='center')
    notes = ['At A, extra O₂ is added: only its line jumps up, at that instant',
             'The system shifts forward to use some up: O₂ falls by x, SO₂ falls by 2x, SO₃ rises by 2x (the equation’s ratio)',
             'At B a new equilibrium: all lines flat. O₂ ends higher than it began (the shift only partly undoes the change), SO₂ lower, SO₃ higher']
    y = 0.78
    for i in range(min(3, s + 1)):
        t_ = fit(ch(notes[i]), 0.32, 20)
        T(fig, 0.62, y, t_, size=20, color=FG if i == min(s, 2) else SOFT)
        y -= frac(20) * (t_.count('\n') + 1) + 0.03


# ============================================================================ calorimeter
def calorimeter(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Calorimetry')
    chip(fig, 'Element 5 · calculations')
    ax = wax(fig, [0.04, 0.12, 0.45, 0.68], (0, 100), (0, 80))
    ax.add_patch(Rectangle((22, 28), 36, 30, fc='#2a5f8f', ec=FG, lw=3, alpha=0.9))
    ax.text(40, 43, 'water\nm, ΔT', color=FG, fontsize=18, ha='center', va='center', weight='bold')
    ax.plot([48, 48], [30, 72], color=FG, lw=3); ax.add_patch(Circle((48, 29), 2.2, fc=PINK, ec='none'))
    ax.text(56, 70, 'thermometer', color=SOFT, fontsize=16)
    ax.add_patch(Rectangle((30, 6), 20, 10, fc='#a05f35', ec=FG, lw=2)); ax.text(40, 11, 'fuel', color=FG, fontsize=16, ha='center', va='center')
    for k in range(3):
        xs = 40 + 2 * (k - 1)
        ax.add_patch(Polygon([[xs - 2.5, 16], [xs + 2.5, 16], [xs + 0.3 * (k - 1), 26]], fc=YELLOW if k == 1 else '#fb923c', ec='none', alpha=0.95))
    ax.text(70, 12, 'Losses: heat to air,\nincomplete burning', color=PINK, fontsize=16, va='center')
    items = ['Heat gained by the water: E = mcΔT. Use the mass of WATER, not the fuel',
             'Moles of fuel: n = m / M. Then ΔH = −E / n in kJ mol⁻¹ (a temperature RISE means an exothermic reaction: negative ΔH)',
             'Convert J to kJ. ΔT in °C equals ΔT in K: do not add 273 to a difference',
             'Result is usually smaller than the data-book value: heat is lost to the surroundings']
    n = min(4, s + 1)
    y = 0.78
    for i in range(n):
        t_ = fit(ch(items[i]), 0.40, 22)
        T(fig, 0.53, y, t_, size=22, color=FG if i == n - 1 else SOFT)
        y -= frac(22) * (t_.count('\n') + 1) + 0.03


# ============================================================================ acids and bases
def acid_particles(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Strong and weak acids')
    chip(fig, 'Element 5 · pH and acids')
    rng = np.random.RandomState(4)
    for k, (title, frac_ion) in enumerate([('Strong acid, e.g. HCl: fully ionised', 1.0), ('Weak acid, e.g. CH₃COOH: slightly ionised', 0.08)]):
        ax = wax(fig, [0.05 + k * 0.47, 0.30, 0.43, 0.48], (0, 10), (0, 10))
        ax.add_patch(Rectangle((0, 0), 10, 10, fc=PANEL, ec=GRID, lw=2))
        ax.text(5, 9.3, title, color=FG, fontsize=18, ha='center', weight='bold')
        n = 12
        pts = rng.uniform(0.8, 9.2, (n, 2)); pts[:, 1] = rng.uniform(0.8, 8.2, n)
        for i, (x, y) in enumerate(pts):
            if i < max(1, int(round(frac_ion * n))) and (frac_ion > 0.5 or i < 1):
                ax.text(x - 0.3, y, 'H⁺', color=C1, fontsize=17, ha='center', va='center', weight='bold')
                ax.text(x + 0.5, y, 'A⁻', color=PINK, fontsize=17, ha='center', va='center', weight='bold')
            else:
                ax.text(x, y, 'HA', color=SOFT, fontsize=17, ha='center', va='center')
    notes = ['Strength = how far the acid ionises at equilibrium, shown by Ka. It is NOT the same as concentration',
             ch('Ka = [H^+][A^-] / [HA]. Strong acids: Ka is so large it is not usually listed. Weak acids: small Ka, and most of the acid stays as HA'),
             'Same concentration: a weak acid has a lower [H⁺] so a HIGHER pH than a strong acid']
    y = 0.24
    for i in range(min(3, s + 1)):
        t_ = fit(notes[i], 0.88, 20)
        T(fig, 0.06, y, t_, size=20, color=FG if i == min(s, 2) else SOFT)
        y -= frac(20) * (t_.count('\n') + 1) + 0.012


def co2_chain(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Linked equilibria: carbon dioxide and the ocean')
    chip(fig, 'Context · carbon dioxide')
    boxes = [('CO₂(g) ⇌ CO₂(aq)', 0.05), ('CO₂ + H₂O ⇌ H₂CO₃', 0.05 + 0.31), ('H₂CO₃ ⇌ H⁺ + HCO₃⁻', 0.05 + 0.62)]
    for i, (t_, x) in enumerate(boxes[: min(3, s + 1)]):
        box(fig, x, 0.60, 0.29, 0.14, fc=PANEL2)
        T(fig, x + 0.145, 0.67, t_, size=21, color=YELLOW, ha='center', va='center')
        if i:
            arrow_x = x - 0.02
            T(fig, arrow_x, 0.67, '→', size=26, color=SOFT, ha='center', va='center')
    if s >= 1:
        box(fig, 0.05, 0.40, 0.44, 0.14, fc=PANEL2)
        T(fig, 0.27, 0.47, 'HCO₃⁻ ⇌ H⁺ + CO₃²⁻', size=21, color=YELLOW, ha='center', va='center')
    if s >= 2:
        box(fig, 0.52, 0.40, 0.43, 0.14, fc=PANEL2)
        T(fig, 0.735, 0.47, 'CaCO₃(s) + H⁺ ⇌ Ca²⁺ + HCO₃⁻', size=21, color=PINK, ha='center', va='center')
    notes = ['More CO₂ in the air shifts the first equilibria right (Le Chatelier): more H₂CO₃, which ionises to release more H⁺: pH falls',
             'Carbonic acid is weak, so only partly ionised, but extra H⁺ still builds up',
             'Shells and plankton are CaCO₃. The extra H⁺ shifts this last equilibrium RIGHT, so shell material dissolves. Do not use HCO₃⁻ going up to explain it: HCO₃⁻ is also used up making CO₃²⁻']
    y = 0.32
    for i in range(min(3, s + 1)):
        t_ = fit(ch(notes[i]), 0.88, 20)
        T(fig, 0.06, y, t_, size=20, color=FG if i == min(s, 2) else SOFT)
        y -= frac(20) * (t_.count('\n') + 1) + 0.012


# ============================================================================ title and thumbnail
def _title_art(fig, rect, ph=0):
    C1, C2 = C()
    ax = wax(fig, rect, (0, 100), (0, 110))
    x = np.linspace(2, 98, 400)
    y = 25 + _profile(x, 55, 25, 30, x0=45, w=11.0) * 0.9
    ax.plot(x, y, color=C1, lw=12)
    ax.plot(x, 25 + _profile(x, 55, 25, 13, x0=45, w=11.0) * 0.9, color=PINK, lw=9, ls='--')
    k = (ph * 1.0) % 1.0
    bx = 2 + 96 * k
    by = float(np.interp(bx, x, y))
    ax.scatter([bx], [by + 5], s=2200, color=YELLOW, edgecolor=BG, linewidth=5, zorder=6)
    ax.annotate('', (14, 28), (14, 79), arrowprops=dict(arrowstyle='<|-|>', color=GREEN, lw=7))
    ax.text(18, 56, 'Ea', color=GREEN, fontsize=60, weight='bold', va='center')
    ax.annotate('', (88, 79), (88, 57), arrowprops=dict(arrowstyle='-|>', color=FG, lw=7))
    ax.text(70, 50, 'ΔH', color=FG, fontsize=60, weight='bold', va='center')
    ax.text(50, 7, '⇌', color=C1, fontsize=110, ha='center', va='center')


def thumbnail(fig):
    C1, C2 = C()
    fig.text(0.04, 0.87, 'CRITERION 6', ha='left', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.04, 0.65, 'Energy,', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.04, 0.44, 'rates &', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.04, 0.23, 'equilibrium', ha='left', va='center', color=FG, fontsize=110, weight='bold')
    _title_art(fig, [0.60, 0.17, 0.38, 0.76])
