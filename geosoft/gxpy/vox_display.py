"""
Geosoft vox display handling

:Classes:

    ==================== ==========================================================================
    :class:`Vox_display` 3D visualization of a vox, which can be placed `geosoft.gxpy.view.View_3d`
    ==================== ==========================================================================
    
.. seealso:: `geosoft.gxpy.vox.Vox`, `geosoft.gxpy.view.View_3d`, `geosoft.gxapi.GXVOXD`

.. note::

    Regression tests provide usage examples:     
    `vox_display tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_vox_display.py>`_

"""
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx
from . import view as gxview
from . import group as gxgroup
from . import vox as gxvox
from . import map as gxmap

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class AggregateException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.vox_display`.

    .. versionadded:: 9.2
    """
    pass

ZONE_DEFAULT = 0 #:
ZONE_LINEAR = 1 #:
ZONE_NORMAL = 2 #:
ZONE_EQUALAREA = 3 #:
ZONE_SHADE = 4 #:
ZONE_LOGLINEAR = 5 #:
ZONE_LAST = 6 #:

class Vox_display:
    """
    Creation and handling of vox displays. Vox displays can be placed into a 3D view for display.

    :Constructors:

        ============= =================================
        :meth:`new`:  create a new vox_display
        ============= =================================
        
    .. versionadded:: 9.3.1
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self):
        if hasattr(self, '_open'):
            if self._open:
                gx.pop_resource(self._open)
                self._open = None
                self._gxvoxd = None
                self._vox = None

    def __init__(self, vox):
        self._gxvoxd = None
        self._vox = vox
        self._open = gx.track_resource(self.__class__.__name__, vox.name)

    @classmethod
    def new(cls, vox):
        """
        Create a new vox_display from a `geosoft.gxpy.vox.Vox` instance.
        
        :param vox: `geosoft.gxpy.vox.Vox` instance

        .. versionadded:: 9.3.1
        """

        voxd = cls(vox)
        color_table = ''
        zone_method = ZONE_DEFAULT
        contour = gxapi.rDUMMY
        voxd._gxvoxd = gxapi.GXVOXD.create(vox.gxvox, color_table, zone_method, contour)
        return voxd

    @classmethod
    def open(cls, gxapi_voxd):
        """
        Create a Vox_display instance from a `gxapi.GXVOXD` instance.

        :param gxapi_voxd: `gxapi.VOXD` instance

        .. versionadded 9.3.1
        """
        name = gxapi.str_ref()
        gxapi_voxd.get_name(name)
        name = os.path.splitext(os.path.basename(name.value))[0]
        vox = gxvox.Vox.open(name, gxapi_vox=gxapi_voxd)
        voxd = cls(vox)
        return voxd

    @property
    def vox(self):
        """ `geosoft.gxpy.vox.Vox` instance"""
        return self._vox

    @property
    def name(self):
        """ instance name, same as the contained Vox name"""
        return self.vox.name

    @property
    def draw_controls(self):
        """
        Vox drawing settings, returned as a tuple:

        (box_on, opacity, extent) as (boolean, float, (min_x, min_y, min_z, max_x, max_y, max_z))

        Can be set.

        .. versionadded:: 9.3.1
        """
        box = gxapi.int_ref()
        trans = gxapi.float_ref()
        x0 = gxapi.float_ref()
        x1 = gxapi.float_ref()
        y0 = gxapi.float_ref()
        y1 = gxapi.float_ref()
        z0 = gxapi.float_ref()
        z1 = gxapi.float_ref()
        self.gxvoxd.get_draw_controls(box, trans, x0, y0, z0, x1, y1, z1)
        return (bool(box.value), trans.value, (x0.value, y0.value, z0.value, x1.value, y1.value, z1.value))

    @draw_controls.setter
    def draw_controls(self, controls):
        box, trans, extent = controls
        x0, y0, z0, x1, y1, z1 = extent
        self.gxvoxd.set_draw_controls(box, trans, x0, y0, z0, x1, y1, z1)

    @property
    def gxvoxd(self):
        """ The :class:`geosoft.gxapi.GXVOXD` instance handle."""
        return self._gxvoxd

    @property
    def is_thematic(self):
        """True if this is a thematic vox display"""
        return bool(self.gxvoxd.is_thematic())

    @property
    def opacity(self):
        """Opacity between 0. (invisible) and 1. (opaque) can be set."""
        return self.draw_controls[1]

    @opacity.setter
    def opacity(self, t):
        controls = list(self.draw_controls)
        controls[1] = t
        self.draw_controls = controls

    @property
    def color_map(self):
        """Return the colour map for this vox"""
        itr = gxapi.GXITR.create()
        self.gxvoxd.get_itr(itr)
        cmap = geosoft.gxpy.group.Color_map(itr)
        cmap.title = self.name
        cmap.unit_of_measure = self.vox.unit_of_measure
        return cmap

    @property
    def shell_limits(self):
        """
        The data limits of the visible data shell for scalar data. Can be set.

        returns: (min, max) limits, data outside this range is transparent, None for no limit

        .. versionadded 9.3.1
        """
        min = gxapi.float_ref()
        max = gxapi.float_ref()
        self.gxvoxd.get_shell_controls(min, max)
        min = min.value
        max = max.value
        if min == gxapi.rDUMMY:
            min = None
        if max == gxapi.rDUMMY:
            max = None
        return min, max

    @shell_limits.setter
    def shell_limits(self, limits):
        min, max = limits
        if min is None:
            min = gxapi.rDUMMY
        if max is None:
            max = gxapi.rDUMMY
        self.gxvoxd.set_shell_controls(min, max)

    def view_3d(self, file_name=None, overwrite=True, plane_2d=False):
        """
        Create a 3d view (`geosoft.gxpy.view.View_3d`)

        :param file_name:   the name of a file for the 3d view. If None a temporary 3d view created.
        :param overwrite:   True to overwrite existing file
        :param plane_2d:    True to keep the 2D plane.  Only keep it if you intend to draw on it otherwise a grey
                            plane will appear in the view.

        .. versionadded:: 9.3
        """

        v3d = gxview.View_3d.new(file_name, overwrite=overwrite)
        gxgroup.Vox_display_group.new(v3d, self)
        if not plane_2d:
            v3d.delete_plane(0)

        return v3d

    def figure_map(self, file_name=None, overwrite=True, title=None, legend_label=None,
                   features=('LEGEND', 'NEATLINE'), **kwargs):
        """
        Create a figure view file from an vox display.

        :param file_name:       the name of a file for the 3d view. If None a temporary 3d view created.
        :param overwrite:       True to overwrite existing file
        :param title:           Title added to the image
        :param legend_label:    If plotting a legend make this the legned title.  The default is the title in the
                                first aggregate layer colour map.
        :param features:        list of features to place on the map, default is ('SCALE', 'LEGEND', 'NEATLINE')

                                    =========== =========================================
                                    'LEGEND'    show the colour legend
                                    'NEATLINE'  draw a neat-line around the image
                                    =========== =========================================

        :param kwargs:          passed to `geosoft.gxpy.map.Map.new`

        .. versionadded:: 9.3
        """

        # uppercase features, use a dict so we pop things we use and report error
        if isinstance(features, str):
            features = (features,)
        feature_list = {}
        if features is not None:
            for f in features:
                feature_list[f.upper()] = None
        features = list(feature_list.keys())

        # setup margins
        if not ('margins' in kwargs):

            bottom_margin = 1.0
            if title:
                bottom_margin += len(title.split('\n')) * 1.0

            right_margin = 1
            if 'LEGEND' in feature_list:
                right_margin += 3.5
            kwargs['margins'] = (1, right_margin, bottom_margin, 1)

        gmap = gxmap.Map.figure((0, 0, 100, 100),
                                file_name=file_name,
                                features=features,
                                title=title,
                                **kwargs)

        with gxview.View.open(gmap, "data") as v:

            if 'LEGEND' in features:
                gxgroup.legend_color_bar(v, 'legend',
                                         title=legend_label,
                                         location=(1, 0),
                                         cmap=self.color_map)

        area = gxview.View.open(gmap, gmap.current_data_view).extent_map_cm()
        area = (area[0] * 10., area[1] * 10., area[2] * 10., area[3] * 10.)

        gmap.create_linked_3d_view(self.view_3d(), area_on_map=area)

        return gmap