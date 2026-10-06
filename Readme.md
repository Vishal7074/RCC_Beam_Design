# 🏗️ RCC Beam Design

An interactive **Reinforced Concrete (RCC) Beam Design** application built using **Python and Streamlit**.

The application performs step-by-step design calculations for a simply supported rectangular RCC beam based on the supplied worked example.

---

## 📖 Problem Statement

A rectangular reinforced concrete beam, located inside a building in a coastal town, is simply supported on two masonry walls 230 mm thick and 6 m apart (centre-to-centre).

The beam has to carry, in addition to its own weight:

- Distributed live load = 10 kN/m
- Dead load = 5 kN/m
- Steel grade = Fe 415

The beam section is designed for maximum moment at midspan.

---

## 🚀 Features

- Interactive beam design inputs
- Automatic recalculation when inputs change
- Effective depth calculation
- Self-weight calculation
- Dead load and live load calculation
- Factored load calculation
- Maximum design moment calculation
- Limiting moment parameter
- Minimum effective depth check
- Required reinforcement area
- Provided reinforcement area
- Steel adequacy check
- Flexural strength check
- Reinforcement detailing
- Clear spacing check
- Deflection control check
- Final beam design summary

---

## 🎛️ Design Inputs

The application allows the user to modify:

### Geometry

- Span
- Masonry wall thickness
- Beam width
- Beam depth
- Nominal maximum aggregate size

### Loads

- Tributary width
- Slab thickness
- Dead load
- Live load
- Load factor

### Materials

- Concrete grade
- Steel grade
- RCC unit weight

### Reinforcement

- Clear cover
- Stirrup diameter
- Main bar diameters
- Number of main bars

---

## 🧮 Design Calculations

The application performs the following major calculations:

### Effective Depth

```text
d = D - clear cover - stirrup diameter - main bar diameter / 2