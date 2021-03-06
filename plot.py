# plotting functions

def raster(spikes):
    fig = make_fig()
    make_raster(fig, spikes)

def colored_raster(spikes, colors):
    fig = make_fig()
    make_raster(fig, spikes, colors)

def tsne(embedding):
    fig = make_fig()
    scatter(embedding)

