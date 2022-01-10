import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib as mpl
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

def basemap_(proj_name='Mercator', facecolor='#ade5f2', central_longitude=0, figsz=(10, 5), dpi=300, img=False, coastlines=False, box_lw=0.5, cn_map=False):
    # basemap

    # Set the projection information
    # https://scitools.org.uk/cartopy/docs/latest/crs/projections.html
    projections = {
        'Robinson': ccrs.Robinson(),
        'PlateCarree': ccrs.PlateCarree(),
        'Mercator': ccrs.Mercator()
        # 'EckertI': ccrs.EckertI,
        # 'EckertII': ccrs.EckertII,
        # 'EckertIII': ccrs.EckertIII,
        # 'EckertIV': ccrs.EckertIV,
        # 'EckertV': ccrs.EckertV,
        # 'EckertVI': ccrs.EckertVI,
        # 'EqualEarth': ccrs.EqualEarth
    }

    # proj = projections[proj_name](central_longitude=central_longitude)
    proj = projections[proj_name]

    # fig initialization
    if cn_map:
        fig = plt.figure(figsize=figsz, dpi=dpi)
        ax = fig.add_axes([0, 0, 1, 1], projection=proj, facecolor=facecolor)
        ax_ = fig.add_axes([0.69, 0.05, 0.24, 0.24], projection=proj, facecolor='none')
        # ax_.set_aspect(1.8)
        plt.setp(ax_.spines.values(), linewidth=0.5)
    else:
        fig = plt.figure(figsize=figsz, dpi=dpi)
        ax = fig.add_subplot(111, projection=proj, facecolor=facecolor)
        ax_ = ''

    # box linewidth
    plt.setp(ax.spines.values(), linewidth=box_lw)

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    ax.set_global()

    # cartopy default landscap and coastline
    if img:
        ax.stock_img()

    if coastlines:
        ax.coastlines()

    return fig, ax, ax_

def stack_image_(fig, ax, lon, lat, data, clim=[], ticks=[], ticklabels=[], unit='', cmap=plt.cm.viridis, remap=True, extend='neither', zorder=0, cb_or='horizontal', cb_middle_label=False, cb_len=0.6, cn_map=False):

    # remap: decide if set_extent. usually turned on for regional plot.

    if not all(np.diff(lat) < 0):
        print('>>> Latitude is not descending! <<<')

    dx = np.diff(lon).mean() / 2
    dy = np.diff(lat).mean() / 2
    extent = [max(np.min(lon) - dx, -179.99), min(np.max(lon) + dx, 179.99), max(np.min(lat) + dy, -89.99), min(np.max(lat) - dy, 89.99)]

    im = ax.imshow(data, extent=extent, transform=ccrs.PlateCarree(), cmap=cmap, zorder=zorder)

    if remap:
        ax.set_extent(extent)

    # about clim
    if clim:
        vmin = clim[0]
        vmax = clim[1]
    else:
        vmin = np.nanmin(data)
        vmax = np.nanmax(data)
        # clim = [vmin, vmax]

    if len(ticks) == 0:
        ticks = list(np.linspace(vmin, vmax, 6))

    if cb_middle_label:
        vmin = vmin - (ticks[1] - ticks[0]) / 2
        vmax = vmax + (ticks[1] - ticks[0]) / 2
        # clim = [vmin, vmax]

    im.set_clim(vmin=vmin, vmax=vmax)

    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

    if cn_map:
        ax.set_extent([71, 138, 18, 50])

    if unit:
        pos = ax.get_position()
        if cb_or == 'horizontal':
            pad = 0.02
            width = 0.03
            cax = fig.add_axes([pos.xmin + (pos.xmax - pos.xmin) * (1 - cb_len) / 2, pos.ymin - pad - width, (pos.xmax - pos.xmin) * cb_len, width])
            cbar = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, extend=extend, orientation=cb_or)
            cbar.ax.get_xaxis().labelpad = 8
            cbar.ax.set_xlabel(unit)
        elif cb_or == 'vertical':
            pad = 0.070
            width = 0.015
            cax = fig.add_axes([pos.xmax + pad, pos.ymin, width, (pos.ymax - pos.ymin)])
            cbar = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, extend=extend, orientation=cb_or)
            cbar.ax.set_ylabel(unit)

        if len(ticks) > 0:
            cbar.set_ticks(ticks)
        cbar.outline.set_visible(True)
        cbar.outline.set_edgecolor('grey')
        cbar.outline.set_linewidth(0.35)

        if len(ticklabels) > 0:
            cbar.set_ticklabels(ticklabels)

    return fig, ax

def stack_shp(ax, shp, facecolor='lightgray', edgecolor='k', linewidth=0.1, alpha=1, zorder=0):

    shp_obj = Reader(shp)
    shape_feature = ShapelyFeature(shp_obj.geometries(), ccrs.PlateCarree())
    ax.add_feature(shape_feature, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth, alpha=alpha, zorder=zorder)

    return ax

def stack_shp_cn(ax, ax_, shp, shp_9d, facecolor='lightgray', edgecolor='k', linewidth=0.1, alpha=1, zorder=0):

    ax.set_extent([71, 138, 18, 50])
    ax = stack_shp(ax, shp, facecolor=facecolor, zorder=zorder, linewidth=linewidth)
    ax = stack_shp(ax, shp_9d, facecolor=facecolor, zorder=zorder, linewidth=linewidth)

    ax_.set_extent([106.55, 123.58, 3, 23.5])
    ax_ = stack_shp(ax_, shp, facecolor=facecolor, zorder=zorder, linewidth=linewidth)
    ax_ = stack_shp(ax_, shp_9d, facecolor=facecolor, zorder=zorder, linewidth=linewidth)

    return ax

def stack_hatch(ax, lon, lat, data='', hatche='////////', style='image', transform=ccrs.PlateCarree(), ms=1, mew=0, mec='k', color='k', zorder=2):

    if len(data) == 0:
        ax.plot(lon, lat, color=color, ls='', marker=hatche, transform=transform, ms=ms, mec=mec, mew=mew, zorder=zorder)
    else:
        if not all(np.diff(lat) < 0):
            print('>>> Latitude is not descending! <<<')

        dx = np.diff(lon).mean() / 2
        dy = np.diff(lat).mean() / 2

        if style == 'image':
            lon_m, lat_m = np.meshgrid(lon - dx, lat - dy)
            ax.pcolor(lon_m, lat_m, data, hatch=hatche, alpha=0, transform=transform, zorder=zorder)

        else:
            ax.contourf(lon, lat, data, 1, hatches=[hatche], alpha=0, transform=transform, zorder=zorder)

    return ax


def upscale(x, ratio, method='mean', skipna=False):
    # x should be numpy array
    if len(x.shape) == 2:
        st = upscale_sub(x, ratio, method=method, skipna=skipna)
    elif len(x.shape) == 3:
        a, b, c = x.shape
        st = np.empty((a, b // ratio, c // ratio))
        for i in range(a):
            st[i, :, :] = upscale_sub(x[i, :, :], ratio, method=method, skipna=skipna)

    return st


def upscale_sub(x, ratio, method='mean', skipna=False):
    # x should be numpy array
    t = x.reshape(x.shape[0] // ratio, ratio, x.shape[1] // ratio, ratio)

    if method == 'mean':
        if not skipna:
            st = np.nanmean(t, axis=(1, 3))
        else:
            st = np.mean(t, axis=(1, 3))
    elif method == 'sum':
        if not skipna:
            st = np.nansum(t, axis=(1, 3))
        else:
            st = np.sum(t, axis=(1, 3))

    return st


