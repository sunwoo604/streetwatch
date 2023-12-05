import images_individual as ii


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'


if __name__== "__main__":
    ii.images_phi(INPUT, OUTPATH)
    ii.images_alex()
    ii.images_brandon(OUTPATH)
    ii.images_kevin('data/kevin_structures.json', OUTPATH)
    ii.images_sunny('data/structure_coordinates.json', OUTPATH)
    ii.images_jonathan('data/jonathan_structures.json', OUTPATH)
    ii.images_derek()
    ii.images_kelly(OUTPATH)
    ii.images_noel(OUTPATH)
    ii.images_joshua('data/joshua_structures.json', OUTPATH)
    ii.images_tram(OUTPATH)
    ii.images_mateo(OUTPATH)
    ii.images_lauren()
