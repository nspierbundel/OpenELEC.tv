if __name__ == '__main__':
    try:
        nParam = len(sys.argv)
        if nParam > 1:
            property = sys.argv[1]
            import cache
            cache.clearProperty(property)
    except Exception, e:
        print str(e)