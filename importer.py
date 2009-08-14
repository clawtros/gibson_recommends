from goodplaces.models import Place

if __name__ == '__main__':
    f = open('places.csv')
    #[Place.objects.create(**d) for d in [[{'name':r[0],'address':r[2]} for r in l.strip().replace('"','').split(',')] for l in f.readlines()]]
    for p in [[r for r in l.strip().replace('"','').split("\t")] for l in f.readlines()]:
        new_place = Place.objects.create(name=p[0], address=p[2]+ ", Vancouver, BC, Canada", description=p[3])
        new_place.tags = p[1]
