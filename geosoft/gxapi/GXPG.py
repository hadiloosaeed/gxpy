### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPG:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPG(0)

    @classmethod
    def null(cls) -> 'GXPG':
        """
        A null (undefined) instance of :class:`GXPG`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# 2D Methods



    def copy(self, p2: 'GXPG') -> None:
        self._wrapper.copy(p2)
        




    def copy_subset(self, p2: 'GXPG', p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None:
        self._wrapper.copy_subset(p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def create(cls, p1: int, p2: int, p3: int) -> 'GXPG':
        ret_val = gxapi_cy.WrapPG.create(GXContext._get_tls_geo(), p2, p3)
        return GXPG(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXPG':
        ret_val = gxapi_cy.WrapPG.create_s(GXContext._get_tls_geo())
        return GXPG(ret_val)






    def dummy(self) -> None:
        self._wrapper.dummy()
        




    def e_type(self) -> int:
        ret_val = self._wrapper.e_type()
        return ret_val




    def n_cols(self) -> int:
        ret_val = self._wrapper.n_cols()
        return ret_val




    def n_rows(self) -> int:
        ret_val = self._wrapper.n_rows()
        return ret_val




    def n_slices(self) -> int:
        ret_val = self._wrapper.n_slices()
        return ret_val




    def range(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.range(p2.value, p3.value)
        




    def get(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get(p2, p3)
        return ret_val




    def read_col(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.read_col(p2, p3, p4, p5)
        




    def read_row(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.read_row(p2, p3, p4, p5)
        




    def re_allocate(self, p2: int, p3: int) -> None:
        self._wrapper.re_allocate(p2, p3)
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2)
        




    def statistics(self, p2: 'GXST') -> None:
        self._wrapper.statistics(p2)
        




    def write_col(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.write_col(p2, p3, p4, p5)
        




    def write_row(self, p2: int, p3: int, p4: int, p5: 'GXVV') -> None:
        self._wrapper.write_row(p2, p3, p4, p5)
        




# 3D Methods



    def copy_subset_3d(self, p2: 'GXPG', p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int, p11: int) -> None:
        self._wrapper.copy_subset_3d(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def create_3d(cls, p1: int, p2: int, p3: int, p4: int) -> 'GXPG':
        ret_val = gxapi_cy.WrapPG.create_3d(GXContext._get_tls_geo(), p2, p3, p4)
        return GXPG(ret_val)




    def read_col_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        self._wrapper.read_col_3d(p2, p3, p4, p5, p6)
        




    def read_row_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        self._wrapper.read_row_3d(p2, p3, p4, p5, p6)
        




    def read_trace_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        self._wrapper.read_trace_3d(p2, p3, p4, p5, p6)
        




    def re_allocate_3d(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.re_allocate_3d(p2, p3, p4)
        




    def write_col_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        self._wrapper.write_col_3d(p2, p3, p4, p5, p6)
        




    def write_row_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        self._wrapper.write_row_3d(p2, p3, p4, p5, p6)
        




    def write_trace_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        self._wrapper.write_trace_3d(p2, p3, p4, p5, p6)
        




# Utility Methods



    def read_bf(self, p2: 'GXBF', p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.read_bf(p2, p3, p4, p5, p6, p7)
        




    def read_ra(self, p2: 'GXRA', p3: int, p4: int, p5: int, p6: int, p7: str) -> None:
        self._wrapper.read_ra(p2, p3, p4, p5, p6, p7.encode())
        




    def write_bf(self, p2: 'GXBF', p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.write_bf(p2, p3, p4, p5, p6, p7)
        




    def write_bf_ex(self, p2: 'GXBF', p3: int, p4: int, p5: int, p6: int, p7: int, p8: float) -> None:
        self._wrapper.write_bf_ex(p2, p3, p4, p5, p6, p7, p8)
        




    def write_wa(self, p2: 'GXWA', p3: int, p4: int, p5: int, p6: int, p7: str) -> None:
        self._wrapper.write_wa(p2, p3, p4, p5, p6, p7.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer