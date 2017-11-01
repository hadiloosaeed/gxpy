### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVAU:
    """
    GXVAU class.

    This is not a class. These are methods that work on
    data stored in `GXVA <geosoft.gxapi.GXVA>` objects
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVAU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVAU`
        
        :returns: A null `GXVAU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVAU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVAU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def prune(cls, v_ap, vv_r, o):
        """
        Prune values from a `GXVA <geosoft.gxapi.GXVA>` based on reference `GXVA <geosoft.gxapi.GXVA>`
        
        :param v_ap:  `GXVA <geosoft.gxapi.GXVA>` to prune
        :param vv_r:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param o:     :ref:`VAU_PRUNE`
        :type  v_ap:  GXVA
        :type  vv_r:  GXVV
        :type  o:     int

        .. versionadded:: 5.0

        **Note:**

        Pruning will shorten the `GXVA <geosoft.gxapi.GXVA>` by removing values
        that are either dummy or non-dummy in the reference
        `GXVA <geosoft.gxapi.GXVA>`
        """
        gxapi_cy.WrapVAU.prune(GXContext._get_tls_geo(), v_ap._wrapper, vv_r._wrapper, o)
        



    @classmethod
    def total_vector(cls, xva, yva, zva, tva):
        """
        Calculate total vector for X,Y and Z components
        
        :param xva:  X Component object
        :param yva:  Y Component object
        :param zva:  Z Component object
        :param tva:  Returned total vector `GXVA <geosoft.gxapi.GXVA>` object
        :type  xva:  GXVA
        :type  yva:  GXVA
        :type  zva:  GXVA
        :type  tva:  GXVA

        .. versionadded:: 5.0
        """
        gxapi_cy.WrapVAU.total_vector(GXContext._get_tls_geo(), xva._wrapper, yva._wrapper, zva._wrapper, tva._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer