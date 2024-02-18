r"""Wrapper for DH_PlaySDK.h

Generated with:
C:\Users\Administrator\Documents\CodeProject\headfile\UnifyNetSDK\gen_ctypes_file\one_dragon_service.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["Libs/win64/play.dll"] = load_library("Libs/win64/play.dll")

# 1 libraries
# End libraries

# No modules

BOOL = c_int# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 131

BYTE = c_ubyte# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 139

WORD = c_ushort# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 140

DWORD = c_ulong# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 141

PBYTE = POINTER(BYTE)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 144

LPBYTE = POINTER(BYTE)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 145

UINT = c_uint# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 159

CHAR = c_char# C:/Program Files/mingw64/x86_64-w64-mingw32/include/winnt.h: 295

LONG = c_long# C:/Program Files/mingw64/x86_64-w64-mingw32/include/winnt.h: 297

LPSTR = POINTER(CHAR)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/winnt.h: 346

LONGLONG = c_int64# C:/Program Files/mingw64/x86_64-w64-mingw32/include/winnt.h: 500

# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 26
class struct_HWND__(Structure):
    pass

struct_HWND__.__slots__ = [
    'unused',
]
struct_HWND__._fields_ = [
    ('unused', c_int),
]

HWND = POINTER(struct_HWND__)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 26

# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 47
class struct_HDC__(Structure):
    pass

struct_HDC__.__slots__ = [
    'unused',
]
struct_HDC__._fields_ = [
    ('unused', c_int),
]

HDC = POINTER(struct_HDC__)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 47

# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwinbase.h: 58
class struct__SYSTEMTIME(Structure):
    pass

struct__SYSTEMTIME.__slots__ = [
    'wYear',
    'wMonth',
    'wDayOfWeek',
    'wDay',
    'wHour',
    'wMinute',
    'wSecond',
    'wMilliseconds',
]
struct__SYSTEMTIME._fields_ = [
    ('wYear', WORD),
    ('wMonth', WORD),
    ('wDayOfWeek', WORD),
    ('wDay', WORD),
    ('wHour', WORD),
    ('wMinute', WORD),
    ('wSecond', WORD),
    ('wMilliseconds', WORD),
]

SYSTEMTIME = struct__SYSTEMTIME# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwinbase.h: 58

enum_anon_396 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_NOTSET = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_GDI = (RENDER_NOTSET + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_X11 = RENDER_GDI# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_DDRAW = (RENDER_X11 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_OPENGL = RENDER_DDRAW# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_D3D = (RENDER_OPENGL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_D3D9 = RENDER_D3D# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_WGL = (RENDER_D3D9 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RENDER_D3D11 = (RENDER_WGL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

RenderType = enum_anon_396# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 144

enum_anon_397 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_NOTSET = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_SW = (DECODE_NOTSET + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_HW = (DECODE_SW + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_HW_FAST = (DECODE_HW + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_MSDK = (DECODE_HW_FAST + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_HW_FAST_D3D11 = (DECODE_MSDK + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DECODE_HW_TEXTURE = (DECODE_HW_FAST_D3D11 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

DecodeType = enum_anon_397# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 154

enum___tPicFormats = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_BMP = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_JPEG = (PicFormat_BMP + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_JPEG_70 = (PicFormat_JPEG + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_JPEG_50 = (PicFormat_JPEG_70 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_JPEG_30 = (PicFormat_JPEG_50 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_JPEG_10 = (PicFormat_JPEG_30 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_BMP24 = (PicFormat_JPEG_10 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_TIFF = (PicFormat_BMP24 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_JPEG_2000 = (PicFormat_TIFF + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

PicFormat_PNG = (PicFormat_JPEG_2000 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

tPicFormats = enum___tPicFormats# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 167

enum__CMD_TYPE = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetTime = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetFileRate = 2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetMediaInfo = 3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetRenderNum = 4# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetRenderTime = 5# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetSrcTime = 6# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetCurRenderNum = 7# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetRenderTimeStamp = 8# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

PLAY_CMD_GetUTCTime = 9# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

CMD_TYPE_E = enum__CMD_TYPE# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 179

enum_anon_398 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 184

AV_SYNC_VIDEO_MASTER = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 184

AV_SYNC_AUDIO_TIME_STAMP = (AV_SYNC_VIDEO_MASTER + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 184

AV_SYNC_TYPE = enum_anon_398# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 184

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 191
class struct__tagRECT(Structure):
    pass

struct__tagRECT.__slots__ = [
    'left',
    'top',
    'right',
    'bottom',
]
struct__tagRECT._fields_ = [
    ('left', LONG),
    ('top', LONG),
    ('right', LONG),
    ('bottom', LONG),
]

DISPLAYRECT = struct__tagRECT# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 191

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 202
class struct__TIME(Structure):
    pass

struct__TIME.__slots__ = [
    'second',
    'minute',
    'hour',
    'day',
    'month',
    'year',
]
struct__TIME._fields_ = [
    ('second', DWORD, 6),
    ('minute', DWORD, 6),
    ('hour', DWORD, 5),
    ('day', DWORD, 5),
    ('month', DWORD, 4),
    ('year', DWORD, 6),
]

USER_TIME = struct__TIME# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 202

pUSER_TIME = POINTER(struct__TIME)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 202

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 225
class struct__FILE_INFO(Structure):
    pass

struct__FILE_INFO.__slots__ = [
    'channel',
    'type',
    'lock_flag',
    'video_audio',
    'image',
    'start_time',
    'end_time',
    'file_length',
    'first_clus_no',
    'ud_no',
    'part',
    'uuid',
    'disk_type',
    'file_type',
    'stream_type',
    'name',
    'rev',
]
struct__FILE_INFO._fields_ = [
    ('channel', UINT),
    ('type', BYTE),
    ('lock_flag', BYTE),
    ('video_audio', BYTE),
    ('image', BYTE),
    ('start_time', USER_TIME),
    ('end_time', USER_TIME),
    ('file_length', UINT),
    ('first_clus_no', UINT),
    ('ud_no', UINT),
    ('part', c_char * int(32)),
    ('uuid', c_char * int(96)),
    ('disk_type', BYTE),
    ('file_type', BYTE),
    ('stream_type', BYTE),
    ('name', c_char * int(64)),
    ('rev', UINT * int(9)),
]

FILE_INFO = struct__FILE_INFO# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 225

pFILE_INFO = POINTER(struct__FILE_INFO)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 225

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 236
class struct_anon_399(Structure):
    pass

struct_anon_399.__slots__ = [
    'nFilePos',
    'nFrameLen',
    'nFrameNum',
    'nFrameTime',
    'nErrorFrameNum',
    'pErrorTime',
    'nErrorLostFrameNum',
    'nErrorFrameSize',
]
struct_anon_399._fields_ = [
    ('nFilePos', LONGLONG),
    ('nFrameLen', LONG),
    ('nFrameNum', LONG),
    ('nFrameTime', LONG),
    ('nErrorFrameNum', LONG),
    ('pErrorTime', POINTER(SYSTEMTIME)),
    ('nErrorLostFrameNum', LONG),
    ('nErrorFrameSize', LONG),
]

FRAME_POS = struct_anon_399# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 236

PFRAME_POS = POINTER(struct_anon_399)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 236

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 244
class struct_anon_400(Structure):
    pass

struct_anon_400.__slots__ = [
    'nWidth',
    'nHeight',
    'nStamp',
    'nType',
    'nFrameRate',
]
struct_anon_400._fields_ = [
    ('nWidth', LONG),
    ('nHeight', LONG),
    ('nStamp', LONG),
    ('nType', LONG),
    ('nFrameRate', LONG),
]

FRAME_INFO = struct_anon_400# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 244

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 266
class struct_anon_401(Structure):
    pass

struct_anon_401.__slots__ = [
    'nFrameType',
    'nFrameSeq',
    'nStamp',
    'nWidth',
    'nHeight',
    'nFrameRate',
    'nChannels',
    'nBitPerSample',
    'nSamplesPerSec',
    'nRemainData',
    'nDataTime',
    'nFrameSubType',
    'nIfMeetGB28181',
    'nGopBitRate',
    'nTotalChannel',
    'nCurChannel',
    'nReserved',
]
struct_anon_401._fields_ = [
    ('nFrameType', c_int),
    ('nFrameSeq', c_int),
    ('nStamp', c_int),
    ('nWidth', c_int),
    ('nHeight', c_int),
    ('nFrameRate', c_int),
    ('nChannels', c_int),
    ('nBitPerSample', c_int),
    ('nSamplesPerSec', c_int),
    ('nRemainData', c_int),
    ('nDataTime', SYSTEMTIME),
    ('nFrameSubType', c_int),
    ('nIfMeetGB28181', c_int),
    ('nGopBitRate', c_int),
    ('nTotalChannel', c_int),
    ('nCurChannel', c_int),
    ('nReserved', c_int * int(54)),
]

FRAME_INFO_EX = struct_anon_401# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 266

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 280
class struct_anon_402(Structure):
    pass

struct_anon_402.__slots__ = [
    'nFrameType',
    'pAudioData',
    'nAudioDataLen',
    'pVideoData',
    'nStride',
    'nWidth',
    'nHeight',
    'nDataTime',
    'nType',
    'nTimeStamp',
    'nReserved',
]
struct_anon_402._fields_ = [
    ('nFrameType', c_int),
    ('pAudioData', POINTER(None)),
    ('nAudioDataLen', c_int),
    ('pVideoData', POINTER(None) * int(3)),
    ('nStride', c_int * int(3)),
    ('nWidth', c_int * int(3)),
    ('nHeight', c_int * int(3)),
    ('nDataTime', SYSTEMTIME),
    ('nType', LONG),
    ('nTimeStamp', c_uint),
    ('nReserved', c_int * int(55)),
]

FRAME_DECODE_INFO = struct_anon_402# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 280

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 289
class struct_anon_403(Structure):
    pass

struct_anon_403.__slots__ = [
    'lWidth',
    'lHeight',
    'lFrameRate',
    'lChannel',
    'lBitPerSample',
    'lSamplesPerSec',
]
struct_anon_403._fields_ = [
    ('lWidth', c_int),
    ('lHeight', c_int),
    ('lFrameRate', c_int),
    ('lChannel', c_int),
    ('lBitPerSample', c_int),
    ('lSamplesPerSec', c_int),
]

MEDIA_INFO = struct_anon_403# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 289

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 290
if _libs["Libs/win64/play.dll"].has("PLAY_GetSdkVersion", "cdecl"):
    PLAY_GetSdkVersion = _libs["Libs/win64/play.dll"].get("PLAY_GetSdkVersion", "cdecl")
    PLAY_GetSdkVersion.argtypes = []
    PLAY_GetSdkVersion.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 291
if _libs["Libs/win64/play.dll"].has("PLAY_GetLastErrorEx", "cdecl"):
    PLAY_GetLastErrorEx = _libs["Libs/win64/play.dll"].get("PLAY_GetLastErrorEx", "cdecl")
    PLAY_GetLastErrorEx.argtypes = []
    PLAY_GetLastErrorEx.restype = DWORD

enum_anon_404 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelUnknown = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelFatal = (LOG_LevelUnknown + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelError = (LOG_LevelFatal + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelWarn = (LOG_LevelError + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelInfo = (LOG_LevelWarn + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelTrace = (LOG_LevelInfo + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LevelDebug = (LOG_LevelTrace + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

LOG_LEVEL = enum_anon_404# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 301

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 302
if _libs["Libs/win64/play.dll"].has("PLAY_SetPrintLogLevel", "cdecl"):
    PLAY_SetPrintLogLevel = _libs["Libs/win64/play.dll"].get("PLAY_SetPrintLogLevel", "cdecl")
    PLAY_SetPrintLogLevel.argtypes = [LOG_LEVEL]
    PLAY_SetPrintLogLevel.restype = None

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 303
if _libs["Libs/win64/play.dll"].has("PLAY_GetFreePort", "cdecl"):
    PLAY_GetFreePort = _libs["Libs/win64/play.dll"].get("PLAY_GetFreePort", "cdecl")
    PLAY_GetFreePort.argtypes = [POINTER(LONG)]
    PLAY_GetFreePort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 304
if _libs["Libs/win64/play.dll"].has("PLAY_ReleasePort", "cdecl"):
    PLAY_ReleasePort = _libs["Libs/win64/play.dll"].get("PLAY_ReleasePort", "cdecl")
    PLAY_ReleasePort.argtypes = [LONG]
    PLAY_ReleasePort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 305
if _libs["Libs/win64/play.dll"].has("PLAY_OpenFile", "cdecl"):
    PLAY_OpenFile = _libs["Libs/win64/play.dll"].get("PLAY_OpenFile", "cdecl")
    PLAY_OpenFile.argtypes = [LONG, LPSTR]
    PLAY_OpenFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 306
if _libs["Libs/win64/play.dll"].has("PLAY_CloseFile", "cdecl"):
    PLAY_CloseFile = _libs["Libs/win64/play.dll"].get("PLAY_CloseFile", "cdecl")
    PLAY_CloseFile.argtypes = [LONG]
    PLAY_CloseFile.restype = BOOL

fFileEndCBFun = CFUNCTYPE(UNCHECKED(None), DWORD, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 307

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 308
if _libs["Libs/win64/play.dll"].has("PLAY_SetFileEndCallBack", "cdecl"):
    PLAY_SetFileEndCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetFileEndCallBack", "cdecl")
    PLAY_SetFileEndCallBack.argtypes = [LONG, fFileEndCBFun, POINTER(None)]
    PLAY_SetFileEndCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 309
if _libs["Libs/win64/play.dll"].has("PLAY_SetStreamOpenMode", "cdecl"):
    PLAY_SetStreamOpenMode = _libs["Libs/win64/play.dll"].get("PLAY_SetStreamOpenMode", "cdecl")
    PLAY_SetStreamOpenMode.argtypes = [LONG, DWORD]
    PLAY_SetStreamOpenMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 310
if _libs["Libs/win64/play.dll"].has("PLAY_GetStreamOpenMode", "cdecl"):
    PLAY_GetStreamOpenMode = _libs["Libs/win64/play.dll"].get("PLAY_GetStreamOpenMode", "cdecl")
    PLAY_GetStreamOpenMode.argtypes = [LONG]
    PLAY_GetStreamOpenMode.restype = LONG

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 311
if _libs["Libs/win64/play.dll"].has("PLAY_OpenStream", "cdecl"):
    PLAY_OpenStream = _libs["Libs/win64/play.dll"].get("PLAY_OpenStream", "cdecl")
    PLAY_OpenStream.argtypes = [LONG, PBYTE, DWORD, DWORD]
    PLAY_OpenStream.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 312
if _libs["Libs/win64/play.dll"].has("PLAY_CloseStream", "cdecl"):
    PLAY_CloseStream = _libs["Libs/win64/play.dll"].get("PLAY_CloseStream", "cdecl")
    PLAY_CloseStream.argtypes = [LONG]
    PLAY_CloseStream.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 313
if _libs["Libs/win64/play.dll"].has("PLAY_InputData", "cdecl"):
    PLAY_InputData = _libs["Libs/win64/play.dll"].get("PLAY_InputData", "cdecl")
    PLAY_InputData.argtypes = [LONG, PBYTE, DWORD]
    PLAY_InputData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 314
if _libs["Libs/win64/play.dll"].has("PLAY_PlaySound", "cdecl"):
    PLAY_PlaySound = _libs["Libs/win64/play.dll"].get("PLAY_PlaySound", "cdecl")
    PLAY_PlaySound.argtypes = [LONG]
    PLAY_PlaySound.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 315
if _libs["Libs/win64/play.dll"].has("PLAY_StopSound", "cdecl"):
    PLAY_StopSound = _libs["Libs/win64/play.dll"].get("PLAY_StopSound", "cdecl")
    PLAY_StopSound.argtypes = []
    PLAY_StopSound.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 316
if _libs["Libs/win64/play.dll"].has("PLAY_PlaySoundShare", "cdecl"):
    PLAY_PlaySoundShare = _libs["Libs/win64/play.dll"].get("PLAY_PlaySoundShare", "cdecl")
    PLAY_PlaySoundShare.argtypes = [LONG]
    PLAY_PlaySoundShare.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 317
if _libs["Libs/win64/play.dll"].has("PLAY_StopSoundShare", "cdecl"):
    PLAY_StopSoundShare = _libs["Libs/win64/play.dll"].get("PLAY_StopSoundShare", "cdecl")
    PLAY_StopSoundShare.argtypes = [LONG]
    PLAY_StopSoundShare.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 318
if _libs["Libs/win64/play.dll"].has("PLAY_SetVolume", "cdecl"):
    PLAY_SetVolume = _libs["Libs/win64/play.dll"].get("PLAY_SetVolume", "cdecl")
    PLAY_SetVolume.argtypes = [LONG, WORD]
    PLAY_SetVolume.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 319
if _libs["Libs/win64/play.dll"].has("PLAY_GetVolume", "cdecl"):
    PLAY_GetVolume = _libs["Libs/win64/play.dll"].get("PLAY_GetVolume", "cdecl")
    PLAY_GetVolume.argtypes = [LONG]
    PLAY_GetVolume.restype = WORD

pCallFunction = CFUNCTYPE(UNCHECKED(None), LPBYTE, DWORD, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 320

enum_anon_405 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_RAW_PCM = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G711A = (AUDIO_RAW_PCM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G711U = (AUDIO_G711A + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_PCM = (AUDIO_G711U + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G7221_ENC = (AUDIO_PCM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G726_40_ENC = (AUDIO_G7221_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G726_32_ENC = (AUDIO_G726_40_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G726_24_ENC = (AUDIO_G726_32_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_G726_16_ENC = (AUDIO_G726_24_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_AAC_ENC = (AUDIO_G726_16_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_AMR_NB_ENC = (AUDIO_AAC_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_CAPTURE_END = (AUDIO_AMR_NB_ENC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

AUDIO_CAPTURE_TYPE = enum_anon_405# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 335

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 336
if _libs["Libs/win64/play.dll"].has("PLAY_OpenAudioRecord", "cdecl"):
    PLAY_OpenAudioRecord = _libs["Libs/win64/play.dll"].get("PLAY_OpenAudioRecord", "cdecl")
    PLAY_OpenAudioRecord.argtypes = [pCallFunction, LONG, LONG, LONG, LONG, POINTER(None)]
    PLAY_OpenAudioRecord.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 337
if _libs["Libs/win64/play.dll"].has("PLAY_CloseAudioRecord", "cdecl"):
    PLAY_CloseAudioRecord = _libs["Libs/win64/play.dll"].get("PLAY_CloseAudioRecord", "cdecl")
    PLAY_CloseAudioRecord.argtypes = []
    PLAY_CloseAudioRecord.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 338
if _libs["Libs/win64/play.dll"].has("PLAY_SpeechChange", "cdecl"):
    PLAY_SpeechChange = _libs["Libs/win64/play.dll"].get("PLAY_SpeechChange", "cdecl")
    PLAY_SpeechChange.argtypes = [BOOL, c_int, c_float]
    PLAY_SpeechChange.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 339
if _libs["Libs/win64/play.dll"].has("PLAY_SetAudioRecScaling", "cdecl"):
    PLAY_SetAudioRecScaling = _libs["Libs/win64/play.dll"].get("PLAY_SetAudioRecScaling", "cdecl")
    PLAY_SetAudioRecScaling.argtypes = [c_float]
    PLAY_SetAudioRecScaling.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 340
if _libs["Libs/win64/play.dll"].has("PLAY_GetAudioRecScaling", "cdecl"):
    PLAY_GetAudioRecScaling = _libs["Libs/win64/play.dll"].get("PLAY_GetAudioRecScaling", "cdecl")
    PLAY_GetAudioRecScaling.argtypes = [POINTER(c_float)]
    PLAY_GetAudioRecScaling.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 341
if _libs["Libs/win64/play.dll"].has("PLAY_SetAudioRenderScaling", "cdecl"):
    PLAY_SetAudioRenderScaling = _libs["Libs/win64/play.dll"].get("PLAY_SetAudioRenderScaling", "cdecl")
    PLAY_SetAudioRenderScaling.argtypes = [LONG, c_float]
    PLAY_SetAudioRenderScaling.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 342
if _libs["Libs/win64/play.dll"].has("PLAY_GetAudioRenderScaling", "cdecl"):
    PLAY_GetAudioRenderScaling = _libs["Libs/win64/play.dll"].get("PLAY_GetAudioRenderScaling", "cdecl")
    PLAY_GetAudioRenderScaling.argtypes = [LONG, POINTER(c_float)]
    PLAY_GetAudioRenderScaling.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 343
if _libs["Libs/win64/play.dll"].has("PLAY_AdjustWaveAudio", "cdecl"):
    PLAY_AdjustWaveAudio = _libs["Libs/win64/play.dll"].get("PLAY_AdjustWaveAudio", "cdecl")
    PLAY_AdjustWaveAudio.argtypes = [LONG, LONG]
    PLAY_AdjustWaveAudio.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 344
if _libs["Libs/win64/play.dll"].has("PLAY_Play", "cdecl"):
    PLAY_Play = _libs["Libs/win64/play.dll"].get("PLAY_Play", "cdecl")
    PLAY_Play.argtypes = [LONG, HWND]
    PLAY_Play.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 345
if _libs["Libs/win64/play.dll"].has("PLAY_Stop", "cdecl"):
    PLAY_Stop = _libs["Libs/win64/play.dll"].get("PLAY_Stop", "cdecl")
    PLAY_Stop.argtypes = [LONG]
    PLAY_Stop.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 346
if _libs["Libs/win64/play.dll"].has("PLAY_Pause", "cdecl"):
    PLAY_Pause = _libs["Libs/win64/play.dll"].get("PLAY_Pause", "cdecl")
    PLAY_Pause.argtypes = [LONG, DWORD]
    PLAY_Pause.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 347
if _libs["Libs/win64/play.dll"].has("PLAY_Slow", "cdecl"):
    PLAY_Slow = _libs["Libs/win64/play.dll"].get("PLAY_Slow", "cdecl")
    PLAY_Slow.argtypes = [LONG]
    PLAY_Slow.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 348
if _libs["Libs/win64/play.dll"].has("PLAY_Fast", "cdecl"):
    PLAY_Fast = _libs["Libs/win64/play.dll"].get("PLAY_Fast", "cdecl")
    PLAY_Fast.argtypes = [LONG]
    PLAY_Fast.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 349
if _libs["Libs/win64/play.dll"].has("PLAY_OneByOne", "cdecl"):
    PLAY_OneByOne = _libs["Libs/win64/play.dll"].get("PLAY_OneByOne", "cdecl")
    PLAY_OneByOne.argtypes = [LONG]
    PLAY_OneByOne.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 350
if _libs["Libs/win64/play.dll"].has("PLAY_OneByOneBack", "cdecl"):
    PLAY_OneByOneBack = _libs["Libs/win64/play.dll"].get("PLAY_OneByOneBack", "cdecl")
    PLAY_OneByOneBack.argtypes = [LONG]
    PLAY_OneByOneBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 351
if _libs["Libs/win64/play.dll"].has("PLAY_SetColor", "cdecl"):
    PLAY_SetColor = _libs["Libs/win64/play.dll"].get("PLAY_SetColor", "cdecl")
    PLAY_SetColor.argtypes = [LONG, DWORD, c_int, c_int, c_int, c_int]
    PLAY_SetColor.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 352
if _libs["Libs/win64/play.dll"].has("PLAY_GetColor", "cdecl"):
    PLAY_GetColor = _libs["Libs/win64/play.dll"].get("PLAY_GetColor", "cdecl")
    PLAY_GetColor.argtypes = [LONG, DWORD, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    PLAY_GetColor.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 353
if _libs["Libs/win64/play.dll"].has("PLAY_SetAVSyncType", "cdecl"):
    PLAY_SetAVSyncType = _libs["Libs/win64/play.dll"].get("PLAY_SetAVSyncType", "cdecl")
    PLAY_SetAVSyncType.argtypes = [LONG, AV_SYNC_TYPE]
    PLAY_SetAVSyncType.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 354
if _libs["Libs/win64/play.dll"].has("PLAY_SetPlaySpeed", "cdecl"):
    PLAY_SetPlaySpeed = _libs["Libs/win64/play.dll"].get("PLAY_SetPlaySpeed", "cdecl")
    PLAY_SetPlaySpeed.argtypes = [LONG, c_float]
    PLAY_SetPlaySpeed.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 355
if _libs["Libs/win64/play.dll"].has("PLAY_SetPlayDirection", "cdecl"):
    PLAY_SetPlayDirection = _libs["Libs/win64/play.dll"].get("PLAY_SetPlayDirection", "cdecl")
    PLAY_SetPlayDirection.argtypes = [LONG, DWORD]
    PLAY_SetPlayDirection.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 356
if _libs["Libs/win64/play.dll"].has("PLAY_SetDelayTime", "cdecl"):
    PLAY_SetDelayTime = _libs["Libs/win64/play.dll"].get("PLAY_SetDelayTime", "cdecl")
    PLAY_SetDelayTime.argtypes = [LONG, c_int, c_int]
    PLAY_SetDelayTime.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 357
if _libs["Libs/win64/play.dll"].has("PLAY_SetPlayMethod", "cdecl"):
    PLAY_SetPlayMethod = _libs["Libs/win64/play.dll"].get("PLAY_SetPlayMethod", "cdecl")
    PLAY_SetPlayMethod.argtypes = [LONG, c_int, c_int, c_int, c_int]
    PLAY_SetPlayMethod.restype = BOOL

enum_anon_406 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 364

CACHE_MODE_OFF = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 364

ADAPTIVE_CACHE = (CACHE_MODE_OFF + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 364

REALTIME_FIRST = (ADAPTIVE_CACHE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 364

FLUENCY_FIRST = (REALTIME_FIRST + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 364

CACHE_MODE = enum_anon_406# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 364

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 365
if _libs["Libs/win64/play.dll"].has("PLAY_SetCacheMode", "cdecl"):
    PLAY_SetCacheMode = _libs["Libs/win64/play.dll"].get("PLAY_SetCacheMode", "cdecl")
    PLAY_SetCacheMode.argtypes = [LONG, CACHE_MODE]
    PLAY_SetCacheMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 366
if _libs["Libs/win64/play.dll"].has("PLAY_SetAudioPlayMethod", "cdecl"):
    PLAY_SetAudioPlayMethod = _libs["Libs/win64/play.dll"].get("PLAY_SetAudioPlayMethod", "cdecl")
    PLAY_SetAudioPlayMethod.argtypes = [LONG, c_int]
    PLAY_SetAudioPlayMethod.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 367
if _libs["Libs/win64/play.dll"].has("PLAY_SetRotateAngle", "cdecl"):
    PLAY_SetRotateAngle = _libs["Libs/win64/play.dll"].get("PLAY_SetRotateAngle", "cdecl")
    PLAY_SetRotateAngle.argtypes = [LONG, c_int]
    PLAY_SetRotateAngle.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 368
if _libs["Libs/win64/play.dll"].has("PLAY_SetPlayPos", "cdecl"):
    PLAY_SetPlayPos = _libs["Libs/win64/play.dll"].get("PLAY_SetPlayPos", "cdecl")
    PLAY_SetPlayPos.argtypes = [LONG, c_float]
    PLAY_SetPlayPos.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 369
if _libs["Libs/win64/play.dll"].has("PLAY_GetPlayPos", "cdecl"):
    PLAY_GetPlayPos = _libs["Libs/win64/play.dll"].get("PLAY_GetPlayPos", "cdecl")
    PLAY_GetPlayPos.argtypes = [LONG]
    PLAY_GetPlayPos.restype = c_float

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 370
if _libs["Libs/win64/play.dll"].has("PLAY_SetPlayedTimeEx", "cdecl"):
    PLAY_SetPlayedTimeEx = _libs["Libs/win64/play.dll"].get("PLAY_SetPlayedTimeEx", "cdecl")
    PLAY_SetPlayedTimeEx.argtypes = [LONG, DWORD]
    PLAY_SetPlayedTimeEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 371
if _libs["Libs/win64/play.dll"].has("PLAY_GetPlayedTimeEx", "cdecl"):
    PLAY_GetPlayedTimeEx = _libs["Libs/win64/play.dll"].get("PLAY_GetPlayedTimeEx", "cdecl")
    PLAY_GetPlayedTimeEx.argtypes = [LONG]
    PLAY_GetPlayedTimeEx.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 372
if _libs["Libs/win64/play.dll"].has("PLAY_GetCurrentFrameNum", "cdecl"):
    PLAY_GetCurrentFrameNum = _libs["Libs/win64/play.dll"].get("PLAY_GetCurrentFrameNum", "cdecl")
    PLAY_GetCurrentFrameNum.argtypes = [LONG]
    PLAY_GetCurrentFrameNum.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 373
if _libs["Libs/win64/play.dll"].has("PLAY_SetCurrentFrameNum", "cdecl"):
    PLAY_SetCurrentFrameNum = _libs["Libs/win64/play.dll"].get("PLAY_SetCurrentFrameNum", "cdecl")
    PLAY_SetCurrentFrameNum.argtypes = [LONG, DWORD]
    PLAY_SetCurrentFrameNum.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 374
if _libs["Libs/win64/play.dll"].has("PLAY_GetPlayedFrames", "cdecl"):
    PLAY_GetPlayedFrames = _libs["Libs/win64/play.dll"].get("PLAY_GetPlayedFrames", "cdecl")
    PLAY_GetPlayedFrames.argtypes = [LONG]
    PLAY_GetPlayedFrames.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 375
if _libs["Libs/win64/play.dll"].has("PLAY_GetPlayedTime", "cdecl"):
    PLAY_GetPlayedTime = _libs["Libs/win64/play.dll"].get("PLAY_GetPlayedTime", "cdecl")
    PLAY_GetPlayedTime.argtypes = [LONG]
    PLAY_GetPlayedTime.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 376
if _libs["Libs/win64/play.dll"].has("PLAY_GetFileTime", "cdecl"):
    PLAY_GetFileTime = _libs["Libs/win64/play.dll"].get("PLAY_GetFileTime", "cdecl")
    PLAY_GetFileTime.argtypes = [LONG]
    PLAY_GetFileTime.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 377
if _libs["Libs/win64/play.dll"].has("PLAY_GetFileTotalFrames", "cdecl"):
    PLAY_GetFileTotalFrames = _libs["Libs/win64/play.dll"].get("PLAY_GetFileTotalFrames", "cdecl")
    PLAY_GetFileTotalFrames.argtypes = [LONG]
    PLAY_GetFileTotalFrames.restype = DWORD

fFileRefDoneCBFun = CFUNCTYPE(UNCHECKED(None), DWORD, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 378

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 379
if _libs["Libs/win64/play.dll"].has("PLAY_SetFileRefCallBack", "cdecl"):
    PLAY_SetFileRefCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetFileRefCallBack", "cdecl")
    PLAY_SetFileRefCallBack.argtypes = [LONG, fFileRefDoneCBFun, POINTER(None)]
    PLAY_SetFileRefCallBack.restype = BOOL

fFileRefDoneCBFunEx = CFUNCTYPE(UNCHECKED(None), DWORD, BOOL, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 382

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 383
if _libs["Libs/win64/play.dll"].has("PLAY_SetFileRefCallBackEx", "cdecl"):
    PLAY_SetFileRefCallBackEx = _libs["Libs/win64/play.dll"].get("PLAY_SetFileRefCallBackEx", "cdecl")
    PLAY_SetFileRefCallBackEx.argtypes = [LONG, fFileRefDoneCBFunEx, POINTER(None)]
    PLAY_SetFileRefCallBackEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 384
if _libs["Libs/win64/play.dll"].has("PLAY_GetKeyFramePos", "cdecl"):
    PLAY_GetKeyFramePos = _libs["Libs/win64/play.dll"].get("PLAY_GetKeyFramePos", "cdecl")
    PLAY_GetKeyFramePos.argtypes = [LONG, DWORD, DWORD, PFRAME_POS]
    PLAY_GetKeyFramePos.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 385
if _libs["Libs/win64/play.dll"].has("PLAY_GetNextKeyFramePos", "cdecl"):
    PLAY_GetNextKeyFramePos = _libs["Libs/win64/play.dll"].get("PLAY_GetNextKeyFramePos", "cdecl")
    PLAY_GetNextKeyFramePos.argtypes = [LONG, DWORD, DWORD, PFRAME_POS]
    PLAY_GetNextKeyFramePos.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 386
if _libs["Libs/win64/play.dll"].has("PLAY_GetRefValue", "cdecl"):
    PLAY_GetRefValue = _libs["Libs/win64/play.dll"].get("PLAY_GetRefValue", "cdecl")
    PLAY_GetRefValue.argtypes = [LONG, POINTER(BYTE), POINTER(DWORD)]
    PLAY_GetRefValue.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 387
if _libs["Libs/win64/play.dll"].has("PLAY_SetRefValue", "cdecl"):
    PLAY_SetRefValue = _libs["Libs/win64/play.dll"].get("PLAY_SetRefValue", "cdecl")
    PLAY_SetRefValue.argtypes = [LONG, POINTER(BYTE), DWORD]
    PLAY_SetRefValue.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 388
if _libs["Libs/win64/play.dll"].has("PLAY_SetDecCBStream", "cdecl"):
    PLAY_SetDecCBStream = _libs["Libs/win64/play.dll"].get("PLAY_SetDecCBStream", "cdecl")
    PLAY_SetDecCBStream.argtypes = [LONG, DWORD]
    PLAY_SetDecCBStream.restype = BOOL

fCBDecode = CFUNCTYPE(UNCHECKED(None), LONG, POINTER(FRAME_DECODE_INFO), POINTER(FRAME_INFO_EX), POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 389

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 390
if _libs["Libs/win64/play.dll"].has("PLAY_SetDecodeCallBack", "cdecl"):
    PLAY_SetDecodeCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetDecodeCallBack", "cdecl")
    PLAY_SetDecodeCallBack.argtypes = [LONG, fCBDecode, POINTER(None)]
    PLAY_SetDecodeCallBack.restype = BOOL

fDisplayCBFun = CFUNCTYPE(UNCHECKED(None), LONG, String, LONG, LONG, LONG, LONG, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 391

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 392
if _libs["Libs/win64/play.dll"].has("PLAY_SetDisplayCallBack", "cdecl"):
    PLAY_SetDisplayCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetDisplayCallBack", "cdecl")
    PLAY_SetDisplayCallBack.argtypes = [LONG, fDisplayCBFun, POINTER(None)]
    PLAY_SetDisplayCallBack.restype = BOOL

fAudioCBFun = CFUNCTYPE(UNCHECKED(None), LONG, String, LONG, LONG, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 393

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 394
if _libs["Libs/win64/play.dll"].has("PLAY_SetAudioCallBack", "cdecl"):
    PLAY_SetAudioCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetAudioCallBack", "cdecl")
    PLAY_SetAudioCallBack.argtypes = [LONG, fAudioCBFun, POINTER(None)]
    PLAY_SetAudioCallBack.restype = BOOL

fVisibleDecodeCallBackFunc = fCBDecode# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 395

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 396
if _libs["Libs/win64/play.dll"].has("PLAY_SetVisibleDecodeCallBack", "cdecl"):
    PLAY_SetVisibleDecodeCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetVisibleDecodeCallBack", "cdecl")
    PLAY_SetVisibleDecodeCallBack.argtypes = [LONG, fVisibleDecodeCallBackFunc, POINTER(None)]
    PLAY_SetVisibleDecodeCallBack.restype = BOOL

fDecCBFun = CFUNCTYPE(UNCHECKED(None), LONG, String, LONG, POINTER(FRAME_INFO), POINTER(None), LONG)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 397

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 398
if _libs["Libs/win64/play.dll"].has("PLAY_SetDecCallBack", "cdecl"):
    PLAY_SetDecCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetDecCallBack", "cdecl")
    PLAY_SetDecCallBack.argtypes = [LONG, fDecCBFun]
    PLAY_SetDecCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 399
if _libs["Libs/win64/play.dll"].has("PLAY_SetDecCallBackEx", "cdecl"):
    PLAY_SetDecCallBackEx = _libs["Libs/win64/play.dll"].get("PLAY_SetDecCallBackEx", "cdecl")
    PLAY_SetDecCallBackEx.argtypes = [LONG, fDecCBFun, POINTER(None)]
    PLAY_SetDecCallBackEx.restype = BOOL

fVisibleDecCBFun = CFUNCTYPE(UNCHECKED(None), LONG, String, LONG, POINTER(FRAME_INFO), POINTER(None), LONG)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 400

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 401
if _libs["Libs/win64/play.dll"].has("PLAY_SetVisibleDecCallBack", "cdecl"):
    PLAY_SetVisibleDecCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetVisibleDecCallBack", "cdecl")
    PLAY_SetVisibleDecCallBack.argtypes = [LONG, fVisibleDecCBFun, POINTER(None)]
    PLAY_SetVisibleDecCallBack.restype = BOOL

fGetWaterMarkInfoCallbackFunc = CFUNCTYPE(UNCHECKED(c_int), String, LONG, LONG, LONG, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 402

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 403
if _libs["Libs/win64/play.dll"].has("PLAY_SetWaterMarkCallBack", "cdecl"):
    PLAY_SetWaterMarkCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetWaterMarkCallBack", "cdecl")
    PLAY_SetWaterMarkCallBack.argtypes = [LONG, fGetWaterMarkInfoCallbackFunc, POINTER(None)]
    PLAY_SetWaterMarkCallBack.restype = BOOL

fGetWaterMarkInfoCallbackFuncEx = CFUNCTYPE(UNCHECKED(c_int), LONG, String, LONG, LONG, LONG, LONG, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 404

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 405
if _libs["Libs/win64/play.dll"].has("PLAY_SetWaterMarkCallBackEx", "cdecl"):
    PLAY_SetWaterMarkCallBackEx = _libs["Libs/win64/play.dll"].get("PLAY_SetWaterMarkCallBackEx", "cdecl")
    PLAY_SetWaterMarkCallBackEx.argtypes = [LONG, fGetWaterMarkInfoCallbackFuncEx, POINTER(None)]
    PLAY_SetWaterMarkCallBackEx.restype = BOOL

fEncChangeCBFun = CFUNCTYPE(UNCHECKED(None), LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 406

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 407
if _libs["Libs/win64/play.dll"].has("PLAY_SetEncTypeChangeCallBack", "cdecl"):
    PLAY_SetEncTypeChangeCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetEncTypeChangeCallBack", "cdecl")
    PLAY_SetEncTypeChangeCallBack.argtypes = [LONG, fEncChangeCBFun, POINTER(None)]
    PLAY_SetEncTypeChangeCallBack.restype = BOOL

fEncChangeCBFunEx = CFUNCTYPE(UNCHECKED(None), LONG, POINTER(None), LONG, LONG)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 408

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 409
if _libs["Libs/win64/play.dll"].has("PLAY_SetEncTypeChangeCallBackEx", "cdecl"):
    PLAY_SetEncTypeChangeCallBackEx = _libs["Libs/win64/play.dll"].get("PLAY_SetEncTypeChangeCallBackEx", "cdecl")
    PLAY_SetEncTypeChangeCallBackEx.argtypes = [LONG, fEncChangeCBFunEx, POINTER(None)]
    PLAY_SetEncTypeChangeCallBackEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 410
if _libs["Libs/win64/play.dll"].has("PLAY_QueryInfo", "cdecl"):
    PLAY_QueryInfo = _libs["Libs/win64/play.dll"].get("PLAY_QueryInfo", "cdecl")
    PLAY_QueryInfo.argtypes = [LONG, c_int, String, c_int, POINTER(c_int)]
    PLAY_QueryInfo.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 411
if _libs["Libs/win64/play.dll"].has("PLAY_GetRealFrameBitRate", "cdecl"):
    PLAY_GetRealFrameBitRate = _libs["Libs/win64/play.dll"].get("PLAY_GetRealFrameBitRate", "cdecl")
    PLAY_GetRealFrameBitRate.argtypes = [LONG, POINTER(c_double)]
    PLAY_GetRealFrameBitRate.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 412
if _libs["Libs/win64/play.dll"].has("PLAY_GetCurrentFrameRate", "cdecl"):
    PLAY_GetCurrentFrameRate = _libs["Libs/win64/play.dll"].get("PLAY_GetCurrentFrameRate", "cdecl")
    PLAY_GetCurrentFrameRate.argtypes = [LONG]
    PLAY_GetCurrentFrameRate.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 413
if _libs["Libs/win64/play.dll"].has("PLAY_GetPictureSize", "cdecl"):
    PLAY_GetPictureSize = _libs["Libs/win64/play.dll"].get("PLAY_GetPictureSize", "cdecl")
    PLAY_GetPictureSize.argtypes = [LONG, POINTER(LONG), POINTER(LONG)]
    PLAY_GetPictureSize.restype = BOOL

enum_anon_407 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 420

FRAME_UNKNOWN = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 420

FRAME_VIDEO = (FRAME_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 420

FRAME_AUDIO = (FRAME_VIDEO + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 420

FRAME_DATA = (FRAME_AUDIO + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 420

FRAME_TYPE = enum_anon_407# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 420

enum_anon_408 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_DATA_INVALID = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_VIDEO_I_FRAME = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_VIDEO_P_FRAME = (FRAME_SUB_TYPE_VIDEO_I_FRAME + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_VIDEO_B_FRAME = (FRAME_SUB_TYPE_VIDEO_P_FRAME + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_VIDEO_SMART_I_FRAME = 19# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_VIDEO_SMART_P_FRAME = 20# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_VIDEO_SMART_I_FRAME_NORENDER = 21# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_DATA_CIPHER_AUXILIARY = 26# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE_DATA_LASER_RADER = 30# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

FRAME_SUB_TYPE = enum_anon_408# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 432

enum_anon_409 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_UNKNOWN = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_MPEG4 = (ENCODE_VIDEO_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_HI_H264 = (ENCODE_VIDEO_MPEG4 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_JPEG = (ENCODE_VIDEO_HI_H264 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_DH_H264 = (ENCODE_VIDEO_JPEG + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_JPEG2000 = 6# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_AVS = 7# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_STD_H264 = 8# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_MPEG2 = 9# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_VNC = 10# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_SVAC = 11# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_DH_H265 = 12# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

ENCODE_VIDEO_TYPE = enum_anon_409# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 447

enum_anon_410 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_UNKNOWN = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_PCM = 7# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G729 = (ENCODE_AUDIO_PCM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_IMA = (ENCODE_AUDIO_G729 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_PCM_MULAW = (ENCODE_AUDIO_IMA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G721 = (ENCODE_PCM_MULAW + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_PCM8_VWIS = (ENCODE_AUDIO_G721 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_MS_ADPCM = (ENCODE_PCM8_VWIS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G711A = (ENCODE_MS_ADPCM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_AMR = (ENCODE_AUDIO_G711A + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_PCM16 = (ENCODE_AUDIO_AMR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G711U = 22# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G723 = 25# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_AAC = (ENCODE_AUDIO_G723 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G726_40 = (ENCODE_AUDIO_AAC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G726_32 = (ENCODE_AUDIO_G726_40 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G726_24 = (ENCODE_AUDIO_G726_32 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G726_16 = (ENCODE_AUDIO_G726_24 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_MP2 = (ENCODE_AUDIO_G726_16 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_OGG = (ENCODE_AUDIO_MP2 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_MP3 = (ENCODE_AUDIO_OGG + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_G722_1 = (ENCODE_AUDIO_MP3 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_OPUS = 38# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

ENCODE_AUDIO_TYPE = enum_anon_410# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 473

enum_anon_411 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_UNKNOWN = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_MPEG4 = (STREAM_TYPE_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_DHPT = 3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_NEW = (STREAM_TYPE_DHPT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_HB = (STREAM_TYPE_NEW + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_AUDIO = (STREAM_TYPE_HB + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_PS = (STREAM_TYPE_AUDIO + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_DHSTD = (STREAM_TYPE_PS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_ASF = (STREAM_TYPE_DHSTD + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_3GPP = (STREAM_TYPE_ASF + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW = (STREAM_TYPE_3GPP + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_TS = (STREAM_TYPE_RAW + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_SVC = (STREAM_TYPE_TS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_AVI = (STREAM_TYPE_SVC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_MP4 = (STREAM_TYPE_AVI + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_CGI = (STREAM_TYPE_MP4 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_WAV = (STREAM_TYPE_CGI + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_FLV = (STREAM_TYPE_WAV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_MKV = (STREAM_TYPE_FLV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RTP = (STREAM_TYPE_MKV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_MPEG4 = (STREAM_TYPE_RTP + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_H264 = (STREAM_TYPE_RAW_MPEG4 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_H265 = (STREAM_TYPE_RAW_H264 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_WMV = (STREAM_TYPE_RAW_H265 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_MPEG2 = (STREAM_TYPE_WMV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_SVAC = (STREAM_TYPE_RAW_MPEG2 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_MOV = (STREAM_TYPE_RAW_SVAC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_VOB = (STREAM_TYPE_MOV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_H263 = (STREAM_TYPE_VOB + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RM = (STREAM_TYPE_RAW_H263 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_DHPS = (STREAM_TYPE_RM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_RAW_AUDIO = (STREAM_TYPE_DHPS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE_HIK_PS = 145# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

STREAM_TYPE = enum_anon_411# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 509

enum_anon_412 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_NOERROR = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_TIMESTAND = (STREAM_ERROR_FLAGS_NOERROR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_LENGTH = (STREAM_ERROR_FLAGS_TIMESTAND + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_HEAD_VERIFY = (STREAM_ERROR_FLAGS_LENGTH + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_DATA_VERIFY = (STREAM_ERROR_FLAGS_HEAD_VERIFY + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_LOST_HEADER = (STREAM_ERROR_FLAGS_DATA_VERIFY + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_UNKNOWN = (STREAM_ERROR_FLAGS_LOST_HEADER + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_LOSTFRAME = (STREAM_ERROR_FLAGS_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_WATERMARK = (STREAM_ERROR_FLAGS_LOSTFRAME + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_CONTEXT = (STREAM_ERROR_FLAGS_WATERMARK + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_NOSUPPORT = (STREAM_ERROR_FLAGS_CONTEXT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_FRAME_HALF_BAKED = (STREAM_ERROR_FLAGS_NOSUPPORT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_SUBTYPE_UNKNOWN = (STREAM_ERROR_FLAGS_FRAME_HALF_BAKED + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR_FLAGS_DECRYPTION_FAILURE = (STREAM_ERROR_FLAGS_SUBTYPE_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

STREAM_ERROR = enum_anon_412# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 526

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 543
class struct_anon_413(Structure):
    pass

struct_anon_413.__slots__ = [
    'pHead',
    'nLen',
    'pBody',
    'nBodyLen',
    'nRet',
    'nEncryptType',
    'nRotateAngle',
    'nCompFrameVerifyStatus',
    'reserved1',
    'nStreamType',
    'nFrameValid',
    'nTotalChannel',
    'nCurChannel',
    'reserved',
]
struct_anon_413._fields_ = [
    ('pHead', String),
    ('nLen', c_int),
    ('pBody', String),
    ('nBodyLen', c_int),
    ('nRet', c_int),
    ('nEncryptType', BYTE),
    ('nRotateAngle', BYTE),
    ('nCompFrameVerifyStatus', c_char),
    ('reserved1', c_char * int(1)),
    ('nStreamType', c_int),
    ('nFrameValid', c_uint),
    ('nTotalChannel', c_ubyte),
    ('nCurChannel', c_ubyte),
    ('reserved', c_char * int(114)),
]

DemuInfoEx = struct_anon_413# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 543

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 563
class struct_anon_414(Structure):
    pass

struct_anon_414.__slots__ = [
    'type',
    'subtype',
    'encode',
    'sequence',
    'width',
    'height',
    'rate',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'secode',
    'timestamp',
    'channels',
    'bitspersample',
    'samplespersecond',
]
struct_anon_414._fields_ = [
    ('type', c_int),
    ('subtype', c_int),
    ('encode', c_int),
    ('sequence', c_int),
    ('width', c_int),
    ('height', c_int),
    ('rate', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('secode', c_int),
    ('timestamp', LONG),
    ('channels', c_int),
    ('bitspersample', c_int),
    ('samplespersecond', c_int),
]

DEMUX_INFO = struct_anon_414# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 563

fDemuxDecCBFun = CFUNCTYPE(UNCHECKED(None), LONG, String, LONG, POINTER(None), POINTER(None), POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 564

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 565
if _libs["Libs/win64/play.dll"].has("PLAY_SetDemuxCallBack", "cdecl"):
    PLAY_SetDemuxCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetDemuxCallBack", "cdecl")
    PLAY_SetDemuxCallBack.argtypes = [LONG, fDemuxDecCBFun, POINTER(None)]
    PLAY_SetDemuxCallBack.restype = BOOL

fH264InfoCBFun = CFUNCTYPE(UNCHECKED(c_int), LONG, String, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 572

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 573
if _libs["Libs/win64/play.dll"].has("PLAY_Set264EncodeInfoCallBack", "cdecl"):
    PLAY_Set264EncodeInfoCallBack = _libs["Libs/win64/play.dll"].get("PLAY_Set264EncodeInfoCallBack", "cdecl")
    PLAY_Set264EncodeInfoCallBack.argtypes = [LONG, fH264InfoCBFun, POINTER(None)]
    PLAY_Set264EncodeInfoCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 574
if _libs["Libs/win64/play.dll"].has("PLAY_SetSecurityKey", "cdecl"):
    PLAY_SetSecurityKey = _libs["Libs/win64/play.dll"].get("PLAY_SetSecurityKey", "cdecl")
    PLAY_SetSecurityKey.argtypes = [LONG, String, DWORD]
    PLAY_SetSecurityKey.restype = BOOL

enum_anon_415 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_UNKOWN = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_AES = (ENCRYPT_UNKOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_AES256 = (ENCRYPT_AES + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_AES256_GDPR2 = (ENCRYPT_AES256 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_SM1_ECB = (ENCRYPT_AES256_GDPR2 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_SM1_OFB = (ENCRYPT_SM1_ECB + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_SM4_ECB = (ENCRYPT_SM1_OFB + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_SM4_OFB = (ENCRYPT_SM4_ECB + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

ENCRYPT_TYPE = enum_anon_415# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 585

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 590
class struct_anon_416(Structure):
    pass

struct_anon_416.__slots__ = [
    'x',
    'y',
]
struct_anon_416._fields_ = [
    ('x', c_ubyte * int(32)),
    ('y', c_ubyte * int(32)),
]

PUBLICKEY_PARAM = struct_anon_416# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 590

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 604
class struct_anon_417(Structure):
    pass

struct_anon_417.__slots__ = [
    'Key',
    'KeyLen',
    'KeyId',
    'KeyIdLen',
    'bSetPublicKey',
    'pPublicKey',
    'pMacKey',
    'nMacKeyLen',
    'nKeyType',
    'nReserved',
    'pReserved',
]
struct_anon_417._fields_ = [
    ('Key', String),
    ('KeyLen', c_int),
    ('KeyId', String),
    ('KeyIdLen', c_int),
    ('bSetPublicKey', c_int),
    ('pPublicKey', POINTER(PUBLICKEY_PARAM)),
    ('pMacKey', String),
    ('nMacKeyLen', c_int),
    ('nKeyType', c_char),
    ('nReserved', c_char * int(15)),
    ('pReserved', POINTER(c_char) * int(12)),
]

DECRYPT_PARAM = struct_anon_417# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 604

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 605
if _libs["Libs/win64/play.dll"].has("PLAY_SetSecurityKeyEx", "cdecl"):
    PLAY_SetSecurityKeyEx = _libs["Libs/win64/play.dll"].get("PLAY_SetSecurityKeyEx", "cdecl")
    PLAY_SetSecurityKeyEx.argtypes = [LONG, ENCRYPT_TYPE, POINTER(DECRYPT_PARAM), c_uint]
    PLAY_SetSecurityKeyEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 606
if _libs["Libs/win64/play.dll"].has("PLAY_SetEncryptKey", "cdecl"):
    PLAY_SetEncryptKey = _libs["Libs/win64/play.dll"].get("PLAY_SetEncryptKey", "cdecl")
    PLAY_SetEncryptKey.argtypes = [LONG, ENCRYPT_TYPE, String, c_uint]
    PLAY_SetEncryptKey.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 607
if _libs["Libs/win64/play.dll"].has("PLAY_SetDisplayRegion", "cdecl"):
    PLAY_SetDisplayRegion = _libs["Libs/win64/play.dll"].get("PLAY_SetDisplayRegion", "cdecl")
    PLAY_SetDisplayRegion.argtypes = [LONG, DWORD, POINTER(DISPLAYRECT), HWND, BOOL]
    PLAY_SetDisplayRegion.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 608
if _libs["Libs/win64/play.dll"].has("PLAY_RefreshPlay", "cdecl"):
    PLAY_RefreshPlay = _libs["Libs/win64/play.dll"].get("PLAY_RefreshPlay", "cdecl")
    PLAY_RefreshPlay.argtypes = [LONG]
    PLAY_RefreshPlay.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 609
if _libs["Libs/win64/play.dll"].has("PLAY_GetSourceBufferRemain", "cdecl"):
    PLAY_GetSourceBufferRemain = _libs["Libs/win64/play.dll"].get("PLAY_GetSourceBufferRemain", "cdecl")
    PLAY_GetSourceBufferRemain.argtypes = [LONG]
    PLAY_GetSourceBufferRemain.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 610
if _libs["Libs/win64/play.dll"].has("PLAY_ResetSourceBuffer", "cdecl"):
    PLAY_ResetSourceBuffer = _libs["Libs/win64/play.dll"].get("PLAY_ResetSourceBuffer", "cdecl")
    PLAY_ResetSourceBuffer.argtypes = [LONG]
    PLAY_ResetSourceBuffer.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 611
if _libs["Libs/win64/play.dll"].has("PLAY_ResetBuffer", "cdecl"):
    PLAY_ResetBuffer = _libs["Libs/win64/play.dll"].get("PLAY_ResetBuffer", "cdecl")
    PLAY_ResetBuffer.argtypes = [LONG, DWORD]
    PLAY_ResetBuffer.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 612
if _libs["Libs/win64/play.dll"].has("PLAY_GetBufferValue", "cdecl"):
    PLAY_GetBufferValue = _libs["Libs/win64/play.dll"].get("PLAY_GetBufferValue", "cdecl")
    PLAY_GetBufferValue.argtypes = [LONG, DWORD]
    PLAY_GetBufferValue.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 613
if _libs["Libs/win64/play.dll"].has("PLAY_InitDisk", "cdecl"):
    PLAY_InitDisk = _libs["Libs/win64/play.dll"].get("PLAY_InitDisk", "cdecl")
    PLAY_InitDisk.argtypes = []
    PLAY_InitDisk.restype = UINT

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 614
if _libs["Libs/win64/play.dll"].has("PLAY_GetDiskType", "cdecl"):
    PLAY_GetDiskType = _libs["Libs/win64/play.dll"].get("PLAY_GetDiskType", "cdecl")
    PLAY_GetDiskType.argtypes = [UINT]
    PLAY_GetDiskType.restype = c_int

fPercentCallbackFunc = CFUNCTYPE(UNCHECKED(None), LONG, c_int, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 615

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 616
if _libs["Libs/win64/play.dll"].has("PLAY_SetPercentCallBack", "cdecl"):
    PLAY_SetPercentCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetPercentCallBack", "cdecl")
    PLAY_SetPercentCallBack.argtypes = [LONG, LONG, LONG, fPercentCallbackFunc, POINTER(None)]
    PLAY_SetPercentCallBack.restype = BOOL

enum_anon_418 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 621

FORMAT_ALL_DATA = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 621

FORMAT_KEY_DATA = (FORMAT_ALL_DATA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 621

FormatType = enum_anon_418# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 621

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 622
if _libs["Libs/win64/play.dll"].has("PLAY_FormatDisk", "cdecl"):
    PLAY_FormatDisk = _libs["Libs/win64/play.dll"].get("PLAY_FormatDisk", "cdecl")
    PLAY_FormatDisk.argtypes = [UINT, FormatType]
    PLAY_FormatDisk.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 623
if _libs["Libs/win64/play.dll"].has("PLAY_QueryFileList", "cdecl"):
    PLAY_QueryFileList = _libs["Libs/win64/play.dll"].get("PLAY_QueryFileList", "cdecl")
    PLAY_QueryFileList.argtypes = [UINT, USER_TIME, USER_TIME, POINTER(UINT), pFILE_INFO, UINT, BYTE, UINT]
    PLAY_QueryFileList.restype = UINT

enum_anon_419 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

FISHEYEMOUNT_MODE_INVALID = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

FISHEYEMOUNT_MODE_CEIL = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

FISHEYEMOUNT_MODE_WALL = (FISHEYEMOUNT_MODE_CEIL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

FISHEYEMOUNT_MODE_FLOOR = (FISHEYEMOUNT_MODE_WALL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

FISHEYEMOUNT_MODE_NUM = (FISHEYEMOUNT_MODE_FLOOR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

FISHEYE_MOUNTMODE = enum_anon_419# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 631

enum_anon_420 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_INVALID = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_OFF = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL = (FISHEYECALIBRATE_MODE_OFF + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PANORAMA = (FISHEYECALIBRATE_MODE_ORIGINAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PANORAMA_PLUS_ONE_EPTZ = (FISHEYECALIBRATE_MODE_PANORAMA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_DOUBLE_PANORAMA = (FISHEYECALIBRATE_MODE_PANORAMA_PLUS_ONE_EPTZ + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_DOUBLE_PANORAMA = (FISHEYECALIBRATE_MODE_DOUBLE_PANORAMA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_THREE_EPTZ_REGION = (FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_DOUBLE_PANORAMA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PANORAMA_PLUS_THREE_EPTZ_REGION = (FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_THREE_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_TWO_EPTZ_REGION = (FISHEYECALIBRATE_MODE_PANORAMA_PLUS_THREE_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_FOUR_EPTZ_REGION = (FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_TWO_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PANORAMA_PLUS_FOUR_EPTZ_REGION = (FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_FOUR_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PANORAMA_PLUS_SIX_EPTZ_REGION = (FISHEYECALIBRATE_MODE_PANORAMA_PLUS_FOUR_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_EIGHT_EPTZ_REGION = (FISHEYECALIBRATE_MODE_PANORAMA_PLUS_SIX_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PANORAMA_PLUS_EIGHT_EPTZ_REGION = (FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_EIGHT_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_TWO_EPTZ_REGION_WITH_ORIGINAL = (FISHEYECALIBRATE_MODE_PANORAMA_PLUS_EIGHT_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_FOUR_EPTZ_REGION_WITH_ORIGINAL = (FISHEYECALIBRATE_MODE_TWO_EPTZ_REGION_WITH_ORIGINAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_DOUBLE_PANORAMA_WITH_ORIGINAL = (FISHEYECALIBRATE_MODE_FOUR_EPTZ_REGION_WITH_ORIGINAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_FOUR_EPTZ_REGION_WITH_PANORAMA = (FISHEYECALIBRATE_MODE_DOUBLE_PANORAMA_WITH_ORIGINAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_TWO_EPTZ_REGION = (FISHEYECALIBRATE_MODE_FOUR_EPTZ_REGION_WITH_PANORAMA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_SINGLE = (FISHEYECALIBRATE_MODE_TWO_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_FOUR_EPTZ_REGION = (FISHEYECALIBRATE_MODE_SINGLE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_USER_DEFINED = (FISHEYECALIBRATE_MODE_FOUR_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_PHONE = (FISHEYECALIBRATE_MODE_USER_DEFINED + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_ONE_EPTZ_REGION = (FISHEYECALIBRATE_MODE_PHONE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_ONE_EPTZ_REGION = (FISHEYECALIBRATE_MODE_ORIGINAL_PLUS_ONE_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_SEMI_SPHERE = (FISHEYECALIBRATE_MODE_ONE_EPTZ_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_CYLINDER = (FISHEYECALIBRATE_MODE_SEMI_SPHERE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_LITTLE_PLANET = (FISHEYECALIBRATE_MODE_CYLINDER + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_DOUBLE_SPHERE = (FISHEYECALIBRATE_MODE_LITTLE_PLANET + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_DOUBLE_CYLINDER = (FISHEYECALIBRATE_MODE_DOUBLE_SPHERE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_DOUBLE_360 = (FISHEYECALIBRATE_MODE_DOUBLE_CYLINDER + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYECALIBRATE_MODE_NUM = (FISHEYECALIBRATE_MODE_DOUBLE_360 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

FISHEYE_CALIBRATMODE = enum_anon_420# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 667

enum_anon_421 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_INVALID = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_ZOOM_IN = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_ZOOM_OUT = (FISHEYEEPTZ_CMD_ZOOM_IN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_UP = (FISHEYEEPTZ_CMD_ZOOM_OUT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_DOWN = (FISHEYEEPTZ_CMD_UP + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_LEFT = (FISHEYEEPTZ_CMD_DOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_RIGHT = (FISHEYEEPTZ_CMD_LEFT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_ROTATE_CLOCKWISE_AUTO = (FISHEYEEPTZ_CMD_RIGHT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_ROTATE_ANTICLOCKWISE_AUTO = (FISHEYEEPTZ_CMD_ROTATE_CLOCKWISE_AUTO + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_STOP = (FISHEYEEPTZ_CMD_ROTATE_ANTICLOCKWISE_AUTO + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_SHOW_REGION = (FISHEYEEPTZ_CMD_STOP + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_EXIT_SHOW_REGION = (FISHEYEEPTZ_CMD_SHOW_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_DEFAULT = (FISHEYEEPTZ_CMD_EXIT_SHOW_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_ORIGIN_ROTATE = (FISHEYEEPTZ_CMD_DEFAULT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_SET_CUR_REGION = 0x20# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_GET_CUR_REGION = (FISHEYEEPTZ_CMD_SET_CUR_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_IS_IN_PANORAMA_REGION = (FISHEYEEPTZ_CMD_GET_CUR_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_TAP_VIEW = (FISHEYEEPTZ_CMD_IS_IN_PANORAMA_REGION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_SET_FOCUS = (FISHEYEEPTZ_CMD_TAP_VIEW + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_GET_FOCUS = (FISHEYEEPTZ_CMD_SET_FOCUS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_PTZ_CALI = (FISHEYEEPTZ_CMD_GET_FOCUS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_GET_PTZ_RLT = (FISHEYEEPTZ_CMD_PTZ_CALI + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_SET_CUR_REGION_PTZ = (FISHEYEEPTZ_CMD_GET_PTZ_RLT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_GET_FOCUS_8192 = (FISHEYEEPTZ_CMD_SET_CUR_REGION_PTZ + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYEEPTZ_CMD_NUM = (FISHEYEEPTZ_CMD_GET_FOCUS_8192 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

FISHEYE_EPTZCMD = enum_anon_421# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 695

enum_anon_422 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 700

FISHEYE_SETPARAM = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 700

FISHEYE_GETPARAM = (FISHEYE_SETPARAM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 700

FISHEYE_OPERATETYPE = enum_anon_422# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 700

enum_anon_423 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

IPCTYPE_200WN = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

IPCTYPE_130WN = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

IPCTYPE_D1WN = 2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

IPCTYPE_100WN = 3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

IPCTYPE_FE = 4# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

SPCTYPE_D6501 = 100# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

HSPCTYPE_D6A2030E = 101# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

HSPCTYPE_D65A2030E = 102# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

CAM_TYPE = enum_anon_423# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 711

enum_anon_424 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LENTYPE_NORM = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LENTYPE_Lens0361 = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LENTYPE_Lens2880 = 2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LENTYPE_Lens0362 = 3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LENTYPE_Lens0401 = 4# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LENTYPE_TEST1 = 100# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

LEN_TYPE = enum_anon_424# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 720

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 725
class struct_anon_425(Structure):
    pass

struct_anon_425.__slots__ = [
    'w',
    'h',
]
struct_anon_425._fields_ = [
    ('w', c_int),
    ('h', c_int),
]

FISHEYE_SIZE = struct_anon_425# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 725

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 730
class struct_anon_426(Structure):
    pass

struct_anon_426.__slots__ = [
    'x',
    'y',
]
struct_anon_426._fields_ = [
    ('x', c_short),
    ('y', c_short),
]

FISHEYE_POINT2D = struct_anon_426# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 730

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 738
class struct_anon_427(Structure):
    pass

struct_anon_427.__slots__ = [
    'subMountMode',
    'subCalibrateMode',
    'imgOutput',
    'upperLeft',
    'reserved',
]
struct_anon_427._fields_ = [
    ('subMountMode', FISHEYE_MOUNTMODE),
    ('subCalibrateMode', FISHEYE_CALIBRATMODE),
    ('imgOutput', FISHEYE_SIZE),
    ('upperLeft', FISHEYE_POINT2D),
    ('reserved', c_int * int(3)),
]

FISHEYE_SUBMODE = struct_anon_427# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 738

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 748
class struct_anon_428(Structure):
    pass

struct_anon_428.__slots__ = [
    'mainShowSize',
    'floatMainShowSize',
    'imgOutput',
    'subMode',
    'subModeNum',
    'outputSizeRatio',
    'reserved',
]
struct_anon_428._fields_ = [
    ('mainShowSize', FISHEYE_SIZE),
    ('floatMainShowSize', FISHEYE_SIZE),
    ('imgOutput', FISHEYE_SIZE),
    ('subMode', POINTER(FISHEYE_SUBMODE)),
    ('subModeNum', c_int),
    ('outputSizeRatio', c_int),
    ('reserved', c_int * int(1)),
]

FISHEYE_OUTPUTFORMAT = struct_anon_428# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 748

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 757
class struct_anon_429(Structure):
    pass

struct_anon_429.__slots__ = [
    'x',
    'y',
    'hAngle',
    'vAngle',
    'available',
    'reserved',
]
struct_anon_429._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('hAngle', c_int),
    ('vAngle', c_int),
    ('available', c_int),
    ('reserved', c_int * int(3)),
]

FISHEYE_REGIONPARAM = struct_anon_429# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 757

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 765
class struct_anon_430(Structure):
    pass

struct_anon_430.__slots__ = [
    'regionParam',
    'circularOffset',
    'panoramaOffset',
    'useRegionParam',
    'reserved',
]
struct_anon_430._fields_ = [
    ('regionParam', FISHEYE_REGIONPARAM * int(9)),
    ('circularOffset', c_int),
    ('panoramaOffset', c_int),
    ('useRegionParam', c_int),
    ('reserved', c_int * int(1)),
]

FISHEYE_MODEINITPARAM = struct_anon_430# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 765

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 795
class struct_anon_431(Structure):
    pass

struct_anon_431.__slots__ = [
    'zoom_type',
    'hcam_wax',
    'hcam_way',
    'hcam_wmul',
    'cfg_type',
    'prm_re',
    'prm_mul',
    'prm_dx',
    'prm_dy',
    'prm_cw',
    'prm_ch',
    'mlen_type',
    'mcam_type',
    'hcam_type',
    'himg_width',
    'himg_height',
    'prm_fax',
    'mcam_fc',
    'mcam_cw',
    'mcam_ch',
    'cam_height',
    'prm_ma',
    'prm_hw',
    'prm_hh',
    'prm_fo',
    'prm_ca',
    'prm_mmul',
]
struct_anon_431._fields_ = [
    ('zoom_type', c_int),
    ('hcam_wax', c_int),
    ('hcam_way', c_int),
    ('hcam_wmul', c_int),
    ('cfg_type', c_int),
    ('prm_re', c_int),
    ('prm_mul', c_int),
    ('prm_dx', c_int),
    ('prm_dy', c_int),
    ('prm_cw', c_int),
    ('prm_ch', c_int),
    ('mlen_type', LEN_TYPE),
    ('mcam_type', CAM_TYPE),
    ('hcam_type', CAM_TYPE),
    ('himg_width', c_int),
    ('himg_height', c_int),
    ('prm_fax', c_int),
    ('mcam_fc', c_int),
    ('mcam_cw', c_int),
    ('mcam_ch', c_int),
    ('cam_height', c_int),
    ('prm_ma', c_int),
    ('prm_hw', c_int),
    ('prm_hh', c_int),
    ('prm_fo', c_int),
    ('prm_ca', c_int),
    ('prm_mmul', c_int),
]

MHFPTZ_CONFIGPARAM = struct_anon_431# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 795

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 814
class struct_anon_432(Structure):
    pass

struct_anon_432.__slots__ = [
    'mainStreamSize',
    'originX',
    'originY',
    'radius',
    'lensDirection',
    'mainMountMode',
    'mainCalibrateMode',
    'modeInitParam',
    'outputFormat',
    'configParam',
    'enableAutoContrast',
    'alphaHistogram',
    'alphaGray',
    'captureSize',
    'mhfptzIndex',
    'reserved',
]
struct_anon_432._fields_ = [
    ('mainStreamSize', FISHEYE_SIZE),
    ('originX', c_int),
    ('originY', c_int),
    ('radius', c_int),
    ('lensDirection', c_int),
    ('mainMountMode', FISHEYE_MOUNTMODE),
    ('mainCalibrateMode', FISHEYE_CALIBRATMODE),
    ('modeInitParam', FISHEYE_MODEINITPARAM),
    ('outputFormat', POINTER(FISHEYE_OUTPUTFORMAT)),
    ('configParam', POINTER(MHFPTZ_CONFIGPARAM)),
    ('enableAutoContrast', c_int),
    ('alphaHistogram', c_int),
    ('alphaGray', c_int),
    ('captureSize', FISHEYE_SIZE),
    ('mhfptzIndex', c_int),
    ('reserved', c_int * int(1)),
]

FISHEYE_OPTPARAM = struct_anon_432# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 814

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 830
class struct_anon_433(Structure):
    pass

struct_anon_433.__slots__ = [
    'ePtzCmd',
    'winId',
    'arg1',
    'arg2',
    'arg3',
    'arg4',
    'arg5',
    'arg6',
    'reserved0',
    'pParam',
    'pResult',
    'pArg',
    'reserved1',
]
struct_anon_433._fields_ = [
    ('ePtzCmd', FISHEYE_EPTZCMD),
    ('winId', c_int),
    ('arg1', c_int),
    ('arg2', c_int),
    ('arg3', c_int),
    ('arg4', c_int),
    ('arg5', c_int),
    ('arg6', c_int),
    ('reserved0', c_int * int(6)),
    ('pParam', POINTER(None)),
    ('pResult', POINTER(None)),
    ('pArg', POINTER(None)),
    ('reserved1', c_int * int(7)),
]

FISHEYE_EPTZPARAM = struct_anon_433# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 830

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 831
if _libs["Libs/win64/play.dll"].has("PLAY_StartFisheye", "cdecl"):
    PLAY_StartFisheye = _libs["Libs/win64/play.dll"].get("PLAY_StartFisheye", "cdecl")
    PLAY_StartFisheye.argtypes = [LONG]
    PLAY_StartFisheye.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 832
if _libs["Libs/win64/play.dll"].has("PLAY_OptFisheyeParams", "cdecl"):
    PLAY_OptFisheyeParams = _libs["Libs/win64/play.dll"].get("PLAY_OptFisheyeParams", "cdecl")
    PLAY_OptFisheyeParams.argtypes = [LONG, FISHEYE_OPERATETYPE, POINTER(FISHEYE_OPTPARAM)]
    PLAY_OptFisheyeParams.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 833
if _libs["Libs/win64/play.dll"].has("PLAY_FisheyeSecondRegion", "cdecl"):
    PLAY_FisheyeSecondRegion = _libs["Libs/win64/play.dll"].get("PLAY_FisheyeSecondRegion", "cdecl")
    PLAY_FisheyeSecondRegion.argtypes = [LONG, HWND, POINTER(FISHEYE_OPTPARAM), BOOL]
    PLAY_FisheyeSecondRegion.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 834
if _libs["Libs/win64/play.dll"].has("PLAY_FisheyeEptzUpdate", "cdecl"):
    PLAY_FisheyeEptzUpdate = _libs["Libs/win64/play.dll"].get("PLAY_FisheyeEptzUpdate", "cdecl")
    PLAY_FisheyeEptzUpdate.argtypes = [LONG, POINTER(FISHEYE_EPTZPARAM), BOOL]
    PLAY_FisheyeEptzUpdate.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 835
if _libs["Libs/win64/play.dll"].has("PLAY_StopFisheye", "cdecl"):
    PLAY_StopFisheye = _libs["Libs/win64/play.dll"].get("PLAY_StopFisheye", "cdecl")
    PLAY_StopFisheye.argtypes = [LONG]
    PLAY_StopFisheye.restype = BOOL

fFishEyeInfoFun = CFUNCTYPE(UNCHECKED(None), LONG, BYTE, WORD, WORD, WORD, UINT, UINT, BYTE, BYTE, BYTE, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 836

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 848
if _libs["Libs/win64/play.dll"].has("PLAY_SetFishEyeInfoCallBack", "cdecl"):
    PLAY_SetFishEyeInfoCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetFishEyeInfoCallBack", "cdecl")
    PLAY_SetFishEyeInfoCallBack.argtypes = [LONG, fFishEyeInfoFun, POINTER(None)]
    PLAY_SetFishEyeInfoCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 849
if _libs["Libs/win64/play.dll"].has("PLAY_CatchPic", "cdecl"):
    PLAY_CatchPic = _libs["Libs/win64/play.dll"].get("PLAY_CatchPic", "cdecl")
    PLAY_CatchPic.argtypes = [LONG, String]
    PLAY_CatchPic.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 850
if _libs["Libs/win64/play.dll"].has("PLAY_CatchPicEx", "cdecl"):
    PLAY_CatchPicEx = _libs["Libs/win64/play.dll"].get("PLAY_CatchPicEx", "cdecl")
    PLAY_CatchPicEx.argtypes = [LONG, String, tPicFormats]
    PLAY_CatchPicEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 851
if _libs["Libs/win64/play.dll"].has("PLAY_ConvertToBmpFile", "cdecl"):
    PLAY_ConvertToBmpFile = _libs["Libs/win64/play.dll"].get("PLAY_ConvertToBmpFile", "cdecl")
    PLAY_ConvertToBmpFile.argtypes = [String, LONG, LONG, LONG, LONG, String]
    PLAY_ConvertToBmpFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 852
if _libs["Libs/win64/play.dll"].has("PLAY_ConvertToJpegFile", "cdecl"):
    PLAY_ConvertToJpegFile = _libs["Libs/win64/play.dll"].get("PLAY_ConvertToJpegFile", "cdecl")
    PLAY_ConvertToJpegFile.argtypes = [String, LONG, LONG, c_int, c_int, String]
    PLAY_ConvertToJpegFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 865
class struct_anon_434(Structure):
    pass

struct_anon_434.__slots__ = [
    'datatype',
    'reserved',
    'inbuf',
    'inbuf_len',
    'width',
    'height',
    'to_formats',
    'outbuf',
    'outbuf_len',
    'reserved1',
]
struct_anon_434._fields_ = [
    ('datatype', c_ubyte),
    ('reserved', c_char * int(3)),
    ('inbuf', POINTER(c_ubyte)),
    ('inbuf_len', c_uint),
    ('width', c_int),
    ('height', c_int),
    ('to_formats', tPicFormats),
    ('outbuf', POINTER(c_ubyte)),
    ('outbuf_len', c_uint),
    ('reserved1', c_char * int(16)),
]

ImageConvertInfo = struct_anon_434# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 865

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 866
if _libs["Libs/win64/play.dll"].has("PLAY_ConvertToImageData", "cdecl"):
    PLAY_ConvertToImageData = _libs["Libs/win64/play.dll"].get("PLAY_ConvertToImageData", "cdecl")
    PLAY_ConvertToImageData.argtypes = [POINTER(ImageConvertInfo)]
    PLAY_ConvertToImageData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 867
if _libs["Libs/win64/play.dll"].has("PLAY_GetPicBMP", "cdecl"):
    PLAY_GetPicBMP = _libs["Libs/win64/play.dll"].get("PLAY_GetPicBMP", "cdecl")
    PLAY_GetPicBMP.argtypes = [LONG, PBYTE, DWORD, POINTER(DWORD)]
    PLAY_GetPicBMP.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 868
if _libs["Libs/win64/play.dll"].has("PLAY_GetPicBMPEx", "cdecl"):
    PLAY_GetPicBMPEx = _libs["Libs/win64/play.dll"].get("PLAY_GetPicBMPEx", "cdecl")
    PLAY_GetPicBMPEx.argtypes = [LONG, PBYTE, DWORD, POINTER(DWORD), LONG, LONG, c_int]
    PLAY_GetPicBMPEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 869
if _libs["Libs/win64/play.dll"].has("PLAY_GetPicJPEG", "cdecl"):
    PLAY_GetPicJPEG = _libs["Libs/win64/play.dll"].get("PLAY_GetPicJPEG", "cdecl")
    PLAY_GetPicJPEG.argtypes = [LONG, PBYTE, DWORD, POINTER(DWORD), c_int]
    PLAY_GetPicJPEG.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 870
if _libs["Libs/win64/play.dll"].has("PLAY_GetPicTIFF", "cdecl"):
    PLAY_GetPicTIFF = _libs["Libs/win64/play.dll"].get("PLAY_GetPicTIFF", "cdecl")
    PLAY_GetPicTIFF.argtypes = [LONG, PBYTE, DWORD, POINTER(DWORD)]
    PLAY_GetPicTIFF.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 871
if _libs["Libs/win64/play.dll"].has("PLAY_CatchResizePic", "cdecl"):
    PLAY_CatchResizePic = _libs["Libs/win64/play.dll"].get("PLAY_CatchResizePic", "cdecl")
    PLAY_CatchResizePic.argtypes = [LONG, String, LONG, LONG, tPicFormats]
    PLAY_CatchResizePic.restype = BOOL

fDrawCBFun = CFUNCTYPE(UNCHECKED(None), LONG, HDC, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 872

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 873
if _libs["Libs/win64/play.dll"].has("PLAY_RigisterDrawFun", "cdecl"):
    PLAY_RigisterDrawFun = _libs["Libs/win64/play.dll"].get("PLAY_RigisterDrawFun", "cdecl")
    PLAY_RigisterDrawFun.argtypes = [LONG, fDrawCBFun, POINTER(None)]
    PLAY_RigisterDrawFun.restype = BOOL

fDrawCBRenderHandleFun = CFUNCTYPE(UNCHECKED(None), LONG, c_int, POINTER(None), POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 874

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 875
if _libs["Libs/win64/play.dll"].has("PLAY_RigisterDrawRendleHandleFun", "cdecl"):
    PLAY_RigisterDrawRendleHandleFun = _libs["Libs/win64/play.dll"].get("PLAY_RigisterDrawRendleHandleFun", "cdecl")
    PLAY_RigisterDrawRendleHandleFun.argtypes = [LONG, fDrawCBRenderHandleFun, POINTER(None)]
    PLAY_RigisterDrawRendleHandleFun.restype = BOOL

fDrawCBFunEx = CFUNCTYPE(UNCHECKED(None), LONG, LONG, HDC, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 876

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 877
if _libs["Libs/win64/play.dll"].has("PLAY_RigisterDrawFunEx", "cdecl"):
    PLAY_RigisterDrawFunEx = _libs["Libs/win64/play.dll"].get("PLAY_RigisterDrawFunEx", "cdecl")
    PLAY_RigisterDrawFunEx.argtypes = [LONG, LONG, fDrawCBFunEx, POINTER(None)]
    PLAY_RigisterDrawFunEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 878
if _libs["Libs/win64/play.dll"].has("PLAY_StartPrepareRecord", "cdecl"):
    PLAY_StartPrepareRecord = _libs["Libs/win64/play.dll"].get("PLAY_StartPrepareRecord", "cdecl")
    PLAY_StartPrepareRecord.argtypes = [LONG, String]
    PLAY_StartPrepareRecord.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 879
if _libs["Libs/win64/play.dll"].has("PLAY_StopPrepareRecord", "cdecl"):
    PLAY_StopPrepareRecord = _libs["Libs/win64/play.dll"].get("PLAY_StopPrepareRecord", "cdecl")
    PLAY_StopPrepareRecord.argtypes = [LONG]
    PLAY_StopPrepareRecord.restype = BOOL

enum_anon_435 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_ORIGINAL = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_AVI = (DATA_RECORD_ORIGINAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_ASF = (DATA_RECORD_AVI + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_ORIGINAL_SEGMENT = (DATA_RECORD_ASF + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_RESIZE_AVI = (DATA_RECORD_ORIGINAL_SEGMENT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_MP4 = (DATA_RECORD_RESIZE_AVI + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_RESIZE_MP4 = (DATA_RECORD_MP4 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_MP4_NOSEEK = (DATA_RECORD_RESIZE_MP4 + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_RESIZE_MP4_NOSEEK = (DATA_RECORD_MP4_NOSEEK + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_TS = (DATA_RECORD_RESIZE_MP4_NOSEEK + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_PS = (DATA_RECORD_TS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_RESIZE_DAV = (DATA_RECORD_PS + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_DAV = (DATA_RECORD_RESIZE_DAV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_AAC = (DATA_RECORD_DAV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_WAV = (DATA_RECORD_AAC + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_FLV = (DATA_RECORD_WAV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_DOUBLE_AUDIO_DAV = (DATA_RECORD_FLV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_ORIGINAL_SEQUENCE = (DATA_RECORD_DOUBLE_AUDIO_DAV + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_COUNT = (DATA_RECORD_ORIGINAL_SEQUENCE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

DATA_RECORD_TYPE = enum_anon_435# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 901

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 902
if _libs["Libs/win64/play.dll"].has("PLAY_StartDataRecord", "cdecl"):
    PLAY_StartDataRecord = _libs["Libs/win64/play.dll"].get("PLAY_StartDataRecord", "cdecl")
    PLAY_StartDataRecord.argtypes = [LONG, String, c_int]
    PLAY_StartDataRecord.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 903
if _libs["Libs/win64/play.dll"].has("PLAY_WriteData", "cdecl"):
    PLAY_WriteData = _libs["Libs/win64/play.dll"].get("PLAY_WriteData", "cdecl")
    PLAY_WriteData.argtypes = [LONG, PBYTE, DWORD]
    PLAY_WriteData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 904
if _libs["Libs/win64/play.dll"].has("PLAY_StopDataRecord", "cdecl"):
    PLAY_StopDataRecord = _libs["Libs/win64/play.dll"].get("PLAY_StopDataRecord", "cdecl")
    PLAY_StopDataRecord.argtypes = [LONG]
    PLAY_StopDataRecord.restype = BOOL

fAVIConvertCallback = CFUNCTYPE(UNCHECKED(None), LONG, LONG, POINTER(None), POINTER(BOOL), String)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 905

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 906
if _libs["Libs/win64/play.dll"].has("PLAY_StartAVIConvert", "cdecl"):
    PLAY_StartAVIConvert = _libs["Libs/win64/play.dll"].get("PLAY_StartAVIConvert", "cdecl")
    PLAY_StartAVIConvert.argtypes = [LONG, String, fAVIConvertCallback, POINTER(None)]
    PLAY_StartAVIConvert.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 907
if _libs["Libs/win64/play.dll"].has("PLAY_StopAVIConvert", "cdecl"):
    PLAY_StopAVIConvert = _libs["Libs/win64/play.dll"].get("PLAY_StopAVIConvert", "cdecl")
    PLAY_StopAVIConvert.argtypes = [LONG]
    PLAY_StopAVIConvert.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 908
if _libs["Libs/win64/play.dll"].has("PLAY_SetEngine", "cdecl"):
    PLAY_SetEngine = _libs["Libs/win64/play.dll"].get("PLAY_SetEngine", "cdecl")
    PLAY_SetEngine.argtypes = [LONG, DecodeType, RenderType]
    PLAY_SetEngine.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 909
if _libs["Libs/win64/play.dll"].has("PLAY_SetPicQuality", "cdecl"):
    PLAY_SetPicQuality = _libs["Libs/win64/play.dll"].get("PLAY_SetPicQuality", "cdecl")
    PLAY_SetPicQuality.argtypes = [LONG, BOOL]
    PLAY_SetPicQuality.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 910
if _libs["Libs/win64/play.dll"].has("PLAY_GetPictureQuality", "cdecl"):
    PLAY_GetPictureQuality = _libs["Libs/win64/play.dll"].get("PLAY_GetPictureQuality", "cdecl")
    PLAY_GetPictureQuality.argtypes = [LONG, POINTER(BOOL)]
    PLAY_GetPictureQuality.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 911
if _libs["Libs/win64/play.dll"].has("PLAY_VerticalSyncEnable", "cdecl"):
    PLAY_VerticalSyncEnable = _libs["Libs/win64/play.dll"].get("PLAY_VerticalSyncEnable", "cdecl")
    PLAY_VerticalSyncEnable.argtypes = [LONG, BOOL]
    PLAY_VerticalSyncEnable.restype = BOOL

enum__PLAY_STRATEGE = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

PLAY_THROW_FRAME_NO = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

PLAY_THROW_FRAME_FLAG_HIGHT = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

PLAY_THROW_FRAME_FLAG_ALL = 2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

PLAY_THROW_FRAME_FLAG_ADAPTION = 3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

PLAY_THROW_FRAME_FLAG_ADAPTION_LOW_CPU = 4# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

PLAY_STRATEGE_E = enum__PLAY_STRATEGE# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 919

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 920
if _libs["Libs/win64/play.dll"].has("PLAY_EnableLargePicAdjustment", "cdecl"):
    PLAY_EnableLargePicAdjustment = _libs["Libs/win64/play.dll"].get("PLAY_EnableLargePicAdjustment", "cdecl")
    PLAY_EnableLargePicAdjustment.argtypes = [LONG, c_int]
    PLAY_EnableLargePicAdjustment.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 921
if _libs["Libs/win64/play.dll"].has("PLAY_SetDecodeThreadNum", "cdecl"):
    PLAY_SetDecodeThreadNum = _libs["Libs/win64/play.dll"].get("PLAY_SetDecodeThreadNum", "cdecl")
    PLAY_SetDecodeThreadNum.argtypes = [LONG, DWORD]
    PLAY_SetDecodeThreadNum.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 922
if _libs["Libs/win64/play.dll"].has("PLAY_SetDecodeStrategy", "cdecl"):
    PLAY_SetDecodeStrategy = _libs["Libs/win64/play.dll"].get("PLAY_SetDecodeStrategy", "cdecl")
    PLAY_SetDecodeStrategy.argtypes = [LONG, c_int]
    PLAY_SetDecodeStrategy.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 923
if _libs["Libs/win64/play.dll"].has("PLAY_AntiAliasEnable", "cdecl"):
    PLAY_AntiAliasEnable = _libs["Libs/win64/play.dll"].get("PLAY_AntiAliasEnable", "cdecl")
    PLAY_AntiAliasEnable.argtypes = [LONG, BOOL]
    PLAY_AntiAliasEnable.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 924
if _libs["Libs/win64/play.dll"].has("PLAY_RenderPrivateData", "cdecl"):
    PLAY_RenderPrivateData = _libs["Libs/win64/play.dll"].get("PLAY_RenderPrivateData", "cdecl")
    PLAY_RenderPrivateData.argtypes = [LONG, BOOL, LONG]
    PLAY_RenderPrivateData.restype = BOOL

enum_anon_436 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_TRACK = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_ALARM = (IVSDRAWER_TRACK + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_RULE = (IVSDRAWER_ALARM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_TRACKEX2 = 14# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_SMARTMOTION = 23# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_DATA_WITH_LARGE_AMOUNT = 25# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

IVSDRAWER_TYPE = enum_anon_436# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 933

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 934
if _libs["Libs/win64/play.dll"].has("PLAY_SetIvsEnable", "cdecl"):
    PLAY_SetIvsEnable = _libs["Libs/win64/play.dll"].get("PLAY_SetIvsEnable", "cdecl")
    PLAY_SetIvsEnable.argtypes = [LONG, c_int, BOOL]
    PLAY_SetIvsEnable.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 941
class struct_anon_437(Structure):
    pass

struct_anon_437.__slots__ = [
    'objtype_enable',
    'attribute88_enable',
    'objid_enable',
    'age_enable',
]
struct_anon_437._fields_ = [
    ('objtype_enable', BOOL),
    ('attribute88_enable', BOOL),
    ('objid_enable', BOOL),
    ('age_enable', BOOL),
]

IVSDRAWER_TrackEx2Config = struct_anon_437# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 941

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 942
if _libs["Libs/win64/play.dll"].has("PLAY_SetIVSTrackEx2Config", "cdecl"):
    PLAY_SetIVSTrackEx2Config = _libs["Libs/win64/play.dll"].get("PLAY_SetIVSTrackEx2Config", "cdecl")
    PLAY_SetIVSTrackEx2Config.argtypes = [c_int, IVSDRAWER_TrackEx2Config]
    PLAY_SetIVSTrackEx2Config.restype = BOOL

fDataCBFun = CFUNCTYPE(UNCHECKED(None), LONG, String, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 943

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 944
if _libs["Libs/win64/play.dll"].has("PLAY_SetDataCallBack", "cdecl"):
    PLAY_SetDataCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetDataCallBack", "cdecl")
    PLAY_SetDataCallBack.argtypes = [LONG, fDataCBFun, POINTER(None)]
    PLAY_SetDataCallBack.restype = BOOL

enum__IVS_TYPE = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_PRESETPOS = 1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_MOTINTRKS = 2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_MOTINTRKS_EX = 3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_LIGHT = 4# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_RAWDATA = 5# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_TRACK = 6# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_TRACK_EX_B0 = 7# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_MOTIONFRAME = 9# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_VIDEO_CONCENTRATION = 10# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_OVERLAY_PIC = 11# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_OSD_INFO = 12# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_GPS_INFO = 13# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_TAGGING_INFO = 14# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_TRACK_A1 = 15# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_DATA_WITH_LARGE_AMOUNT = 16# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_TRACK_A1_EX = 17# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_DATA_WITH_WATER_LEVEL_MONITOR = 18# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_INTELFLOW = 19# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_DATA_WITH_SOUND_DECIBEL = 20# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_DATA_WITH_SMART_MOTION = 21# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_DHOP_SMART = 22# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_TRAFFIC_LIGHT = 23# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVSINFOTYPE_PTZ_LOCATION = 24# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

IVS_TYPE = enum__IVS_TYPE# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 970

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 976
class struct_anon_438(Structure):
    pass

struct_anon_438.__slots__ = [
    'nOverLayPicPurpose',
    'nOverLayPicAction',
    'nOverLayPicCodeFormat',
]
struct_anon_438._fields_ = [
    ('nOverLayPicPurpose', c_ubyte),
    ('nOverLayPicAction', c_ubyte),
    ('nOverLayPicCodeFormat', c_ubyte),
]

OVERLAY_PIC_INFO = struct_anon_438# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 976

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 985
class struct_anon_439(Structure):
    pass

struct_anon_439.__slots__ = [
    'nOsdTopLeftCornercoordinateX',
    'nOsdTopLeftCornercoordinateY',
    'nOsdWordSize',
    'nOsdWordAlignment',
    'reverse',
    'nOsdRgbaValue',
]
struct_anon_439._fields_ = [
    ('nOsdTopLeftCornercoordinateX', c_ushort),
    ('nOsdTopLeftCornercoordinateY', c_ushort),
    ('nOsdWordSize', c_ubyte),
    ('nOsdWordAlignment', c_ubyte),
    ('reverse', c_ubyte * int(6)),
    ('nOsdRgbaValue', c_uint),
]

OSD_DATA_INFO = struct_anon_439# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 985

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 993
class struct_anon_440(Structure):
    pass

struct_anon_440.__slots__ = [
    'version',
    'redLight',
    'yellowLight',
    'greenLight',
    'reverse',
]
struct_anon_440._fields_ = [
    ('version', c_ubyte),
    ('redLight', c_ubyte),
    ('yellowLight', c_ubyte),
    ('greenLight', c_ubyte),
    ('reverse', c_ubyte * int(4)),
]

TRAFFIC_LIGHT_INFO = struct_anon_440# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 993

fIVSInfoCallbackFunc = CFUNCTYPE(UNCHECKED(None), String, LONG, LONG, LONG, POINTER(None), POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 994

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 995
if _libs["Libs/win64/play.dll"].has("PLAY_SetIVSCallBack", "cdecl"):
    PLAY_SetIVSCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetIVSCallBack", "cdecl")
    PLAY_SetIVSCallBack.argtypes = [LONG, fIVSInfoCallbackFunc, POINTER(None)]
    PLAY_SetIVSCallBack.restype = BOOL

fGPSInfoCallbackFunc = CFUNCTYPE(UNCHECKED(c_int), String, LONG, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 996

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 997
if _libs["Libs/win64/play.dll"].has("PLAY_SetGPSCallBack", "cdecl"):
    PLAY_SetGPSCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetGPSCallBack", "cdecl")
    PLAY_SetGPSCallBack.argtypes = [LONG, fGPSInfoCallbackFunc, POINTER(None)]
    PLAY_SetGPSCallBack.restype = BOOL

enum__PARSE_ERROR_FLAGS = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_NOERROR = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_TIMESTAND = (PARSE_ERROR_FLAGS_NOERROR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_LENGTH = (PARSE_ERROR_FLAGS_TIMESTAND + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_HEAD_VERIFY = (PARSE_ERROR_FLAGS_LENGTH + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_DATA_VERIFY = (PARSE_ERROR_FLAGS_HEAD_VERIFY + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_LOST_HEADER = (PARSE_ERROR_FLAGS_DATA_VERIFY + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_UNKNOWN = (PARSE_ERROR_FLAGS_LOST_HEADER + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_LOSTFRAME = (PARSE_ERROR_FLAGS_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_WATERMARK = (PARSE_ERROR_FLAGS_LOSTFRAME + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_CONTEXT = (PARSE_ERROR_FLAGS_WATERMARK + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_NOSUPPORT = (PARSE_ERROR_FLAGS_CONTEXT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_FRAME_HALF_BAKED = (PARSE_ERROR_FLAGS_NOSUPPORT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_SUBTYPE_UNKNOWN = (PARSE_ERROR_FLAGS_FRAME_HALF_BAKED + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS_DECRYPTION_FAILURE = (PARSE_ERROR_FLAGS_SUBTYPE_UNKNOWN + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

PARSE_ERROR_FLAGS = enum__PARSE_ERROR_FLAGS# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1014

enum__STATISTIC_TYPE = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

TYPE_UNUSE = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

INPUT_DATA_INTERVAL = (TYPE_UNUSE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

PRASE_VIDEO_INTERVAL = (INPUT_DATA_INTERVAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_PTS_INTERVAL = (PRASE_VIDEO_INTERVAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

DECODE_VIDEO_TIME = (VIDEO_PTS_INTERVAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

PLAY_VIDEO_INTERVAL = (DECODE_VIDEO_TIME + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

RENDER_VIDEO_TIME = (PLAY_VIDEO_INTERVAL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_DECODE_GOP_AVERAGE = (RENDER_VIDEO_TIME + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_DECODE_ERROR = 1000# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_PARSE_ERROR = (VIDEO_DECODE_ERROR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_RENDER_ERROR = (VIDEO_PARSE_ERROR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_DECODE_SWITCH = (VIDEO_RENDER_ERROR + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_PLAY_MODE = (VIDEO_DECODE_SWITCH + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_FRAME_DURATION = (VIDEO_PLAY_MODE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

VIDEO_INPUT_GOP_AVERAGE = (VIDEO_FRAME_DURATION + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

PLAY_VIDEO_CALLBACK_INTERVAL = (VIDEO_INPUT_GOP_AVERAGE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

STATISTIC_TYPE = enum__STATISTIC_TYPE# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1033

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1041
class struct_statistic_info(Structure):
    pass

struct_statistic_info.__slots__ = [
    'nPort',
    'nStatisticType',
    'nParam1',
    'nParam2',
    'szReserved',
]
struct_statistic_info._fields_ = [
    ('nPort', LONG),
    ('nStatisticType', LONG),
    ('nParam1', LONGLONG),
    ('nParam2', LONGLONG),
    ('szReserved', c_char * int(16)),
]

STATISTIC_INFO = struct_statistic_info# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1041

PSTATISTIC_INFO = POINTER(struct_statistic_info)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1041

fStatisticCallbackFunc = CFUNCTYPE(UNCHECKED(c_int), PSTATISTIC_INFO, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1042

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1043
if _libs["Libs/win64/play.dll"].has("PLAY_SetStatisticCallBack", "cdecl"):
    PLAY_SetStatisticCallBack = _libs["Libs/win64/play.dll"].get("PLAY_SetStatisticCallBack", "cdecl")
    PLAY_SetStatisticCallBack.argtypes = [LONG, fStatisticCallbackFunc, POINTER(None)]
    PLAY_SetStatisticCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1044
if _libs["Libs/win64/play.dll"].has("PLAY_SetViewProportion", "cdecl"):
    PLAY_SetViewProportion = _libs["Libs/win64/play.dll"].get("PLAY_SetViewProportion", "cdecl")
    PLAY_SetViewProportion.argtypes = [LONG, c_int, c_int]
    PLAY_SetViewProportion.restype = BOOL

enum_anon_441 = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE_VOICE = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE_SYSTEM = (AUDIO_PLAYBACK_MODE_VOICE + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE_RING = (AUDIO_PLAYBACK_MODE_SYSTEM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE_MEDIA = (AUDIO_PLAYBACK_MODE_RING + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE_ALARM = (AUDIO_PLAYBACK_MODE_MEDIA + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE_NOTIFICATION = (AUDIO_PLAYBACK_MODE_ALARM + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

AUDIO_PLAYBACK_MODE = enum_anon_441# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1053

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1054
if _libs["Libs/win64/play.dll"].has("PLAY_SetAudioPlaybackMode", "cdecl"):
    PLAY_SetAudioPlaybackMode = _libs["Libs/win64/play.dll"].get("PLAY_SetAudioPlaybackMode", "cdecl")
    PLAY_SetAudioPlaybackMode.argtypes = [LONG, AUDIO_PLAYBACK_MODE]
    PLAY_SetAudioPlaybackMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1055
if _libs["Libs/win64/play.dll"].has("PLAY_ViewResolutionChanged", "cdecl"):
    PLAY_ViewResolutionChanged = _libs["Libs/win64/play.dll"].get("PLAY_ViewResolutionChanged", "cdecl")
    PLAY_ViewResolutionChanged.argtypes = [LONG, c_int, c_int, DWORD]
    PLAY_ViewResolutionChanged.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1061
class struct_profiled_window_mask(Structure):
    pass

struct_profiled_window_mask.__slots__ = [
    'pMaskData',
    'width',
    'height',
]
struct_profiled_window_mask._fields_ = [
    ('pMaskData', String),
    ('width', c_uint),
    ('height', c_uint),
]

ProfieldWindowMask = struct_profiled_window_mask# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1061

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1062
if _libs["Libs/win64/play.dll"].has("PLAY_DrawProfiledWindow", "cdecl"):
    PLAY_DrawProfiledWindow = _libs["Libs/win64/play.dll"].get("PLAY_DrawProfiledWindow", "cdecl")
    PLAY_DrawProfiledWindow.argtypes = [LONG, BOOL, POINTER(ProfieldWindowMask)]
    PLAY_DrawProfiledWindow.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1063
if _libs["Libs/win64/play.dll"].has("PLAY_EnableAutoTrack", "cdecl"):
    PLAY_EnableAutoTrack = _libs["Libs/win64/play.dll"].get("PLAY_EnableAutoTrack", "cdecl")
    PLAY_EnableAutoTrack.argtypes = [LONG, BOOL, c_int]
    PLAY_EnableAutoTrack.restype = BOOL

fAutoTrackInfoCallbackFunc = CFUNCTYPE(UNCHECKED(None), BOOL, POINTER(None))# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1064

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1080
class struct_auto_track_config(Structure):
    pass

struct_auto_track_config.__slots__ = [
    'nTrackRegionNum',
    'nTrackHWnd',
    'nGeneralViewRegionNum',
    'nGeneralViewHWnd',
    'nObjType',
    'pAutoTrackFunc',
    'x',
    'y',
    'xSize',
    'ySize',
    'minXSize',
    'minYSize',
    'pUserData',
]
struct_auto_track_config._fields_ = [
    ('nTrackRegionNum', c_uint),
    ('nTrackHWnd', HWND),
    ('nGeneralViewRegionNum', c_uint),
    ('nGeneralViewHWnd', HWND),
    ('nObjType', c_uint),
    ('pAutoTrackFunc', fAutoTrackInfoCallbackFunc),
    ('x', c_int),
    ('y', c_int),
    ('xSize', c_int),
    ('ySize', c_int),
    ('minXSize', c_int),
    ('minYSize', c_int),
    ('pUserData', POINTER(None)),
]

AutoTrackConfig = struct_auto_track_config# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1080

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1081
if _libs["Libs/win64/play.dll"].has("PLAY_SetMutiWindowAutoTrack", "cdecl"):
    PLAY_SetMutiWindowAutoTrack = _libs["Libs/win64/play.dll"].get("PLAY_SetMutiWindowAutoTrack", "cdecl")
    PLAY_SetMutiWindowAutoTrack.argtypes = [LONG, POINTER(AutoTrackConfig), BOOL]
    PLAY_SetMutiWindowAutoTrack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1082
if _libs["Libs/win64/play.dll"].has("PLAY_GetLastError", "cdecl"):
    PLAY_GetLastError = _libs["Libs/win64/play.dll"].get("PLAY_GetLastError", "cdecl")
    PLAY_GetLastError.argtypes = [LONG]
    PLAY_GetLastError.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1083
if _libs["Libs/win64/play.dll"].has("PLAY_CreateFile", "cdecl"):
    PLAY_CreateFile = _libs["Libs/win64/play.dll"].get("PLAY_CreateFile", "cdecl")
    PLAY_CreateFile.argtypes = [LPSTR]
    PLAY_CreateFile.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1084
if _libs["Libs/win64/play.dll"].has("PLAY_DestroyFile", "cdecl"):
    PLAY_DestroyFile = _libs["Libs/win64/play.dll"].get("PLAY_DestroyFile", "cdecl")
    PLAY_DestroyFile.argtypes = [LONG]
    PLAY_DestroyFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1085
if _libs["Libs/win64/play.dll"].has("PLAY_CreateStream", "cdecl"):
    PLAY_CreateStream = _libs["Libs/win64/play.dll"].get("PLAY_CreateStream", "cdecl")
    PLAY_CreateStream.argtypes = [DWORD]
    PLAY_CreateStream.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1086
if _libs["Libs/win64/play.dll"].has("PLAY_DestroyStream", "cdecl"):
    PLAY_DestroyStream = _libs["Libs/win64/play.dll"].get("PLAY_DestroyStream", "cdecl")
    PLAY_DestroyStream.argtypes = [LONG]
    PLAY_DestroyStream.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1087
if _libs["Libs/win64/play.dll"].has("PLAY_BackOne", "cdecl"):
    PLAY_BackOne = _libs["Libs/win64/play.dll"].get("PLAY_BackOne", "cdecl")
    PLAY_BackOne.argtypes = [LONG]
    PLAY_BackOne.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1088
if _libs["Libs/win64/play.dll"].has("PLAY_SetEncChangeMsg", "cdecl"):
    PLAY_SetEncChangeMsg = _libs["Libs/win64/play.dll"].get("PLAY_SetEncChangeMsg", "cdecl")
    PLAY_SetEncChangeMsg.argtypes = [LONG, HWND, UINT]
    PLAY_SetEncChangeMsg.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1089
if _libs["Libs/win64/play.dll"].has("PLAY_SetFileEndMsg", "cdecl"):
    PLAY_SetFileEndMsg = _libs["Libs/win64/play.dll"].get("PLAY_SetFileEndMsg", "cdecl")
    PLAY_SetFileEndMsg.argtypes = [LONG, HWND, UINT]
    PLAY_SetFileEndMsg.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 63
try:
    FUNC_MAX_PORT = 511
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 64
try:
    MIN_WAVE_COEF = (-100)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 65
try:
    MAX_WAVE_COEF = 100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 66
try:
    MIN_AUDIO_RECORD_LEN = 320
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 67
try:
    MAX_AUDIO_RECORD_LEN = 4096
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 68
try:
    MAX_DISPLAY_WND = 64
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 69
try:
    BUF_VIDEO_SRC = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 70
try:
    BUF_AUDIO_SRC = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 71
try:
    BUF_VIDEO_RENDER = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 72
try:
    BUF_AUDIO_RENDER = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 73
try:
    BUF_VIDEO_ALL = 5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 74
try:
    BY_FRAMENUM = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 75
try:
    BY_FRAMETIME = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 76
try:
    SOURCE_BUF_MAX = (1024 * 100000)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 77
try:
    SOURCE_BUF_MIN = (1024 * 1024)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 78
try:
    STREAME_REALTIME = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 79
try:
    STREAME_FILE = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 80
try:
    T_AUDIO16 = 101
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 81
try:
    T_AUDIO8 = 100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 82
try:
    T_UYVY = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 83
try:
    T_IYUV = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 84
try:
    T_NV12 = 5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 85
try:
    T_RGB32 = 7
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 86
try:
    AVI_MEDIACHANGE_FRAMERATE = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 87
try:
    AVI_MEDIACHANGE_RESOLUTION = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 88
try:
    WATERMARK_DATA_TEXT = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 89
try:
    WATERMARK_DATA_JPEG_BMP = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 90
try:
    WATERMARK_DATA_FRAMEDATA = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 91
try:
    PLAY_NOERROR = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 92
try:
    PLAY_COMMON_ERROR = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 93
try:
    PLAY_PARA_INVALID = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 94
try:
    PLAY_ORDER_ERROR = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 95
try:
    PLAY_PORT_OPEN = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 96
try:
    PLAY_PORT_CLOSE = 5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 97
try:
    PLAY_PORT_INVALID = 6
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 98
try:
    PLAY_PORT_EXIST = 7
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 99
try:
    PLAY_OPEN_FILE_ERROR = 8
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 100
try:
    PLAY_INTERFACE_NOT_SUPPORT = 9
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 101
try:
    PLAY_HWND_INVALID = 10
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 102
try:
    PLAY_PLAY_ERROR = 11
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 103
try:
    PLAY_SPEED_INVALID = 12
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 104
try:
    PLAY_NOT_FILE = 13
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 105
try:
    PLAY_NOT_STREAM = 14
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 106
try:
    PLAY_NO_FRAME = 15
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 107
try:
    PLAY_INDEX_NOT_COMPLETE = 16
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 108
try:
    PLAY_INDEX_COMPLETE = 17
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 109
try:
    PLAY_GET_FILE_SIZE_ERROR = 18
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 110
try:
    PLAY_CREATE_THREAD_FAIL = 19
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 111
try:
    PLAY_CREATE_EVENT_FAIL = 20
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 112
try:
    PLAY_SOUND_SHARE_MODE = 21
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 113
try:
    PLAY_INCLUDE_SOUND_SHARE_PORT = 22
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 114
try:
    PLAY_NOT_INCLUDE_SOUND_SHARE_PORT = 23
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 115
try:
    PLAY_CREATE_DIR_ERROR = 24
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 116
try:
    PLAY_CREATE_FILE_ERROR = 25
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 117
try:
    PLAY_CONVERT_YUV_ERROR = 26
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 118
try:
    PLAY_CONVERT_JPG_ERROR = 27
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 119
try:
    PLAY_CONVERT_BMP_ERROR = 28
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 120
try:
    PLAY_CONVERT_TIFF_ERROR = 29
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 121
try:
    PLAY_HW_CATCH_ERROR = 30
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 122
try:
    PLAY_CREATE_VIDEO_RENDER_ERROR = 31
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 123
try:
    PLAY_NOT_SUPPORT_REF_VALUE = 32
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 124
try:
    PLAY_FORMAT_NOT_SUPPORT = 33
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 125
try:
    PLAY_CREATE_RECORD_ERROR = 34
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 126
try:
    PLAY_OPEN_RECORD_ERROR = 35
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 127
try:
    PLAY_FRAMERATE_ERROR = 36
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 128
try:
    PLAY_CREATE_AUDIO_RECORD_ERROR = 37
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 129
try:
    PLAY_OPEN_AUDIO_RECORD_ERROR = 38
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 130
try:
    PLAY_AES_ALLOC_ERROR = 39
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 131
try:
    PLAY_BUF_OVER = 40
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 132
try:
    PLAY_ALLOC_MEMORY_ERROR = 41
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 204
try:
    UUID_MAX_LEN = 96
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 205
try:
    MAX_DEV_NAME_LEN = 32
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 247
try:
    FRAME_TYPE_VIDEO = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 248
try:
    FRAME_TYPE_AUDIO = 1
except:
    pass

_tagRECT = struct__tagRECT# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 191

_TIME = struct__TIME# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 202

_FILE_INFO = struct__FILE_INFO# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 225

statistic_info = struct_statistic_info# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1041

profiled_window_mask = struct_profiled_window_mask# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1061

auto_track_config = struct_auto_track_config# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_PlaySDK.h: 1080

# No inserted files

# No prefix-stripping

