text = ("PEP stands for Python Enhancement Proposal, "
        "and there are many PEPs. These documents primarily "
        "describe new features proposed for the Python "
        "language, but some PEPs also focus on design and "
        "style and aim to serve as a resource for the community. "
        "PEP 8 is one of these style-focused PEPs.")

if lang(text)>50:
        return f'{text[:50]}...'