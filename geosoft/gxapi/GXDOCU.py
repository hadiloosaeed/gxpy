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
class GXDOCU:
    """
    GXDOCU class.

    Class to work with documents
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDOCU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDOCU`
        
        :returns: A null `GXDOCU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDOCU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDOCU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, doc_us):
        """
        Copy `GXDOCU <geosoft.gxapi.GXDOCU>`
        
        :param doc_us:  Source `GXDOCU <geosoft.gxapi.GXDOCU>`
        :type  doc_us:  GXDOCU

        .. versionadded:: 5.1.1
        """
        self._wrapper.copy(doc_us._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create a document onject
        

        :returns:    `GXDOCU <geosoft.gxapi.GXDOCU>` Object
        :rtype:      GXDOCU

        .. versionadded:: 5.1.1
        """
        ret_val = gxapi_cy.WrapDOCU.create(GXContext._get_tls_geo())
        return GXDOCU(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create from a serialized source
        
        :param bf:  `GXBF <geosoft.gxapi.GXBF>` from which to read `GXDOCU <geosoft.gxapi.GXDOCU>`
        :type  bf:  GXBF

        :returns:    `GXDOCU <geosoft.gxapi.GXDOCU>` Object
        :rtype:      GXDOCU

        .. versionadded:: 5.1.1
        """
        ret_val = gxapi_cy.WrapDOCU.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXDOCU(ret_val)






    def get_file(self, file):
        """
        Get the document and place in a file.
        
        :param file:  File to which to write document
        :type  file:  str

        .. versionadded:: 5.1.1
        """
        self._wrapper.get_file(file.encode())
        




    def get_file_meta(self, file):
        """
        Get the document and place in a file with metadata.
        
        :param file:  File to which to write document
        :type  file:  str

        .. versionadded:: 5.1.8

        **Note:**

        If this document is only a URL link, the URL link will
        be resolved and the document downloaded from the appropriate
        server using the protocol specified.
        
        The document has metadata, and the native document does not
        support metadata, the metadata will be placed in an associated
        file "filename.extension.GeosoftMeta"
        """
        self._wrapper.get_file_meta(file.encode())
        




    def get_meta(self, meta):
        """
        Get the document's meta
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to fill in with the document's meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1.1
        """
        self._wrapper.get_meta(meta._wrapper)
        




    def doc_name(self, name):
        """
        The document name.
        
        :param name:  Buffer to fill with document name
        :type  name:  str_ref

        .. versionadded:: 5.1.1
        """
        name.value = self._wrapper.doc_name(name.value.encode())
        




    def file_name(self, name):
        """
        The original document file name.
        
        :param name:  Buffer to fill with document file name
        :type  name:  str_ref

        .. versionadded:: 5.1.1
        """
        name.value = self._wrapper.file_name(name.value.encode())
        




    def have_meta(self):
        """
        Checks if a document has metadata.
        
        :rtype:       bool

        .. versionadded:: 5.1.1
        """
        ret_val = self._wrapper.have_meta()
        return ret_val




    def is_reference(self):
        """
        Is the document only a reference (a URL) ?
        

        :returns:     1 - Yes, 0 - No
        :rtype:       int

        .. versionadded:: 5.1.6
        """
        ret_val = self._wrapper.is_reference()
        return ret_val




    def open(self, mode):
        """
        Open a document in the document viewer
        
        :param mode:  :ref:`DOCU_OPEN`
        :type  mode:  int

        .. versionadded:: 5.1.1

        **Note:**

        On Windows, the default application for the file extension is
        used to open the file.
        """
        self._wrapper.open(mode)
        




    def serial(self, bf):
        """
        Serialize `GXDOCU <geosoft.gxapi.GXDOCU>`
        
        :param bf:    `GXBF <geosoft.gxapi.GXBF>` in which to write object
        :type  bf:    GXBF

        .. versionadded:: 5.1.1
        """
        self._wrapper.serial(bf._wrapper)
        




    def set_file(self, type, name, file):
        """
        Set the document from a file source.
        
        :param type:  Document type
        :param name:  Document name, if "" file name will be used
        :param file:  Document file, must exist
        :type  type:  str
        :type  name:  str
        :type  file:  str

        .. versionadded:: 5.1.1

        **Note:**

        Document types are normally identified by their extension.  If you
        leave the document type blank, the extension of the document file
        will be used as the document type.
        
        To resolve conflicting types, you can define your own unique type
        by entering your own type "extension" string.
        
        The following types are pre-defined (as are any normal Geosoft
        file types):
        
           "htm"       HTML
           "html"      HTML
           "txt"       ASCII text file
           "doc"       Word for Windows document
           "pdf"       Adobe PDF
           "map"       Geosoft map file
           "mmap"      Mapinfo map file (real extension "map")
           "grd"       Geosoft grid file
           "gdb"       Geosoft database
        
        URL Document Links
        
        The document name can be a URL link to the document using one of
        the supported protocols. The following protocols are supported:
        
           http://www.mywebserver.com/MyFile.doc                 - `GXHTTP <geosoft.gxapi.GXHTTP>`
           dap://my.dap.server.com/dcs?DatasetName?MyFile.doc    - DAP (DAP Document Access)
           ftp://my.ftp.server.com/Dir1/MyFile.doc               - FTP protocol
        
        The full file name will be stored but no data will be stored with
        the `GXDOCU <geosoft.gxapi.GXDOCU>` class and the document can be retrieved using the sGetFile_DOCU
        method.
        """
        self._wrapper.set_file(type.encode(), name.encode(), file.encode())
        




    def set_file_meta(self, type, name, file):
        """
        Set the document from a file source with metadata.
        
        :param type:  Document type extension
        :param name:  Document name, if NULL use file name
        :param file:  Document file or URL
        :type  type:  str
        :type  name:  str
        :type  file:  str

        .. versionadded:: 5.1.8

        **Note:**

        See `set_file <geosoft.gxapi.GXDOCU.set_file>`.
        This function is the same as sSetFile_DOCU, plus insures that a
        `GXMETA <geosoft.gxapi.GXMETA>` exists that includes the "Data" class.  If the file has
        associated metadata, either supported natively in the file, or
        through an associated file "filename.extension.GeosoftMeta",
        that metadata will be loaded into the `GXDOCU <geosoft.gxapi.GXDOCU>` meta, and a Data
        class will be constructed if one does not exist.
        
        Also, the Document type Extension is very important in that it
        specifies the document types that natively have metadata. The
        ones currently supported are:
        
           "map"       Geosoft map file
           "gdb"       Geosoft database
           "grd"       Geosoft grid file
        """
        self._wrapper.set_file_meta(type.encode(), name.encode(), file.encode())
        




    def set_meta(self, meta):
        """
        Set the document's meta
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` to add to the document's meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1.1
        """
        self._wrapper.set_meta(meta._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer