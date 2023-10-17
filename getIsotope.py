def getIsotope(el, nucleons):
    # Get isotope of element
    for iso in el.isotopes:
        if iso.mass_number == nucleons:
            return iso