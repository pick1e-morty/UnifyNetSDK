r"""Wrapper for HK_PlaySDK.h

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
_libs["lib/win/PlayCtrl.dll"] = load_library("lib/win/PlayCtrl.dll")

# 1 libraries
# End libraries

# No modules

BOOL = c_int# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 131

BYTE = c_ubyte# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 139

WORD = c_ushort# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 140

DWORD = c_ulong# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 141

PBYTE = POINTER(BYTE)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 144

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

# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 56
class struct_HMONITOR__(Structure):
    pass

struct_HMONITOR__.__slots__ = [
    'unused',
]
struct_HMONITOR__._fields_ = [
    ('unused', c_int),
]

HMONITOR = POINTER(struct_HMONITOR__)# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 56

COLORREF = DWORD# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 61

# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 78
class struct_tagRECT(Structure):
    pass

struct_tagRECT.__slots__ = [
    'left',
    'top',
    'right',
    'bottom',
]
struct_tagRECT._fields_ = [
    ('left', LONG),
    ('top', LONG),
    ('right', LONG),
    ('bottom', LONG),
]

RECT = struct_tagRECT# C:/Program Files/mingw64/x86_64-w64-mingw32/include/windef.h: 78

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

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 162
class struct_anon_396(Structure):
    pass

struct_anon_396.__slots__ = [
    'nFilePos',
    'nFrameNum',
    'nFrameTime',
    'nErrorFrameNum',
    'pErrorTime',
    'nErrorLostFrameNum',
    'nErrorFrameSize',
]
struct_anon_396._fields_ = [
    ('nFilePos', LONGLONG),
    ('nFrameNum', c_long),
    ('nFrameTime', c_long),
    ('nErrorFrameNum', c_long),
    ('pErrorTime', POINTER(SYSTEMTIME)),
    ('nErrorLostFrameNum', c_long),
    ('nErrorFrameSize', c_long),
]

FRAME_POS = struct_anon_396# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 162

PFRAME_POS = POINTER(struct_anon_396)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 162

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 171
class struct_anon_397(Structure):
    pass

struct_anon_397.__slots__ = [
    'nWidth',
    'nHeight',
    'nStamp',
    'nType',
    'nFrameRate',
    'dwFrameNum',
]
struct_anon_397._fields_ = [
    ('nWidth', c_long),
    ('nHeight', c_long),
    ('nStamp', c_long),
    ('nType', c_long),
    ('nFrameRate', c_long),
    ('dwFrameNum', DWORD),
]

FRAME_INFO = struct_anon_397# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 171

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 179
class struct_anon_398(Structure):
    pass

struct_anon_398.__slots__ = [
    'pDataBuf',
    'nSize',
    'nFrameNum',
    'bIsAudio',
    'nReserved',
]
struct_anon_398._fields_ = [
    ('pDataBuf', String),
    ('nSize', c_long),
    ('nFrameNum', c_long),
    ('bIsAudio', BOOL),
    ('nReserved', c_long),
]

FRAME_TYPE = struct_anon_398# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 179

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 187
class struct_anon_399(Structure):
    pass

struct_anon_399.__slots__ = [
    'pDataBuf',
    'nSize',
    'nFrameNum',
    'bRsaRight',
    'nReserved',
]
struct_anon_399._fields_ = [
    ('pDataBuf', String),
    ('nSize', c_long),
    ('nFrameNum', c_long),
    ('bRsaRight', BOOL),
    ('nReserved', c_long),
]

WATERMARK_INFO = struct_anon_399# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 187

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 193
class struct_SYNCDATA_INFO(Structure):
    pass

struct_SYNCDATA_INFO.__slots__ = [
    'dwDataType',
    'dwDataLen',
    'pData',
]
struct_SYNCDATA_INFO._fields_ = [
    ('dwDataType', DWORD),
    ('dwDataLen', DWORD),
    ('pData', POINTER(BYTE)),
]

SYNCDATA_INFO = struct_SYNCDATA_INFO# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 193

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 200
class struct__VCA_RECT_F_(Structure):
    pass

struct__VCA_RECT_F_.__slots__ = [
    'x',
    'y',
    'width',
    'height',
]
struct__VCA_RECT_F_._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('width', c_float),
    ('height', c_float),
]

VCA_RECT_F = struct__VCA_RECT_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 200

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 207
class struct_anon_400(Structure):
    pass

struct_anon_400.__slots__ = [
    'privt_type',
    'reseverd',
    'privt_len',
    'privt_data',
]
struct_anon_400._fields_ = [
    ('privt_type', c_ubyte),
    ('reseverd', c_ubyte * int(6)),
    ('privt_len', c_ubyte),
    ('privt_data', c_ubyte * int(32)),
]

IS_PRIVT_INFO = struct_anon_400# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 207

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 214
class struct_anon_401(Structure):
    pass

struct_anon_401.__slots__ = [
    'red',
    'green',
    'blue',
    'alpha',
]
struct_anon_401._fields_ = [
    ('red', c_ubyte),
    ('green', c_ubyte),
    ('blue', c_ubyte),
    ('alpha', c_ubyte),
]

IS_PRIVT_INFO_COLOR = struct_anon_401# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 214

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 222
class struct_anon_402(Structure):
    pass

struct_anon_402.__slots__ = [
    'color',
    'confidence',
    'pos_len',
    'pos_data',
    'type',
]
struct_anon_402._fields_ = [
    ('color', IS_PRIVT_INFO_COLOR),
    ('confidence', c_ubyte),
    ('pos_len', c_ubyte),
    ('pos_data', c_ubyte * int(22)),
    ('type', c_uint),
]

IS_PRIVT_INFO_CONTRABAND = struct_anon_402# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 222

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 229
class struct__VCA_TARGET_EX(Structure):
    pass

struct__VCA_TARGET_EX.__slots__ = [
    'ID',
    'reserved',
    'rect',
    'reserved1',
]
struct__VCA_TARGET_EX._fields_ = [
    ('ID', c_uint),
    ('reserved', c_ubyte * int(8)),
    ('rect', VCA_RECT_F),
    ('reserved1', c_ubyte * int(40)),
]

VCA_TARGET_EX = struct__VCA_TARGET_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 229

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 234
class struct__VCA_TARGET_LIST_EX(Structure):
    pass

struct__VCA_TARGET_LIST_EX.__slots__ = [
    'target_num',
    'pstTarget',
]
struct__VCA_TARGET_LIST_EX._fields_ = [
    ('target_num', c_uint),
    ('pstTarget', POINTER(VCA_TARGET_EX)),
]

VCA_TARGET_LIST_EX = struct__VCA_TARGET_LIST_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 234

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 240
class struct__INTEL_INFO_EX(Structure):
    pass

struct__INTEL_INFO_EX.__slots__ = [
    'type',
    'stTarget',
    'stTarget_EX',
]
struct__INTEL_INFO_EX._fields_ = [
    ('type', c_uint),
    ('stTarget', VCA_TARGET_LIST_EX),
    ('stTarget_EX', VCA_TARGET_LIST_EX),
]

INTEL_INFO_EX = struct__INTEL_INFO_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 240

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 245
class struct__VCA_POINT_F_(Structure):
    pass

struct__VCA_POINT_F_.__slots__ = [
    'x',
    'y',
]
struct__VCA_POINT_F_._fields_ = [
    ('x', c_float),
    ('y', c_float),
]

VCA_POINT_F = struct__VCA_POINT_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 245

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 250
class struct__VCA_POLYGON_F_(Structure):
    pass

struct__VCA_POLYGON_F_.__slots__ = [
    'vertex_num',
    'point',
]
struct__VCA_POLYGON_F_._fields_ = [
    ('vertex_num', c_uint),
    ('point', VCA_POINT_F * int(10)),
]

VCA_POLYGON_F = struct__VCA_POLYGON_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 250

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 258
class struct__VCA_ROTATE_RECT_F_(Structure):
    pass

struct__VCA_ROTATE_RECT_F_.__slots__ = [
    'cx',
    'cy',
    'width',
    'height',
    'theta',
]
struct__VCA_ROTATE_RECT_F_._fields_ = [
    ('cx', c_float),
    ('cy', c_float),
    ('width', c_float),
    ('height', c_float),
    ('theta', c_float),
]

VCA_ROTATE_RECT_F = struct__VCA_ROTATE_RECT_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 258

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 263
class union_anon_403(Union):
    pass

union_anon_403.__slots__ = [
    'size',
    'polygon',
    'rect',
    'rotate_rect',
]
union_anon_403._fields_ = [
    ('size', c_ubyte * int(84)),
    ('polygon', VCA_POLYGON_F),
    ('rect', VCA_RECT_F),
    ('rotate_rect', VCA_ROTATE_RECT_F),
]

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 270
class struct__VCA_REGION_(Structure):
    pass

struct__VCA_REGION_.__slots__ = [
    'region_type',
    'reserved',
    'unnamed_1',
]
struct__VCA_REGION_._anonymous_ = [
    'unnamed_1',
]
struct__VCA_REGION_._fields_ = [
    ('region_type', c_uint),
    ('reserved', c_char * int(12)),
    ('unnamed_1', union_anon_403),
]

VCA_REGION = struct__VCA_REGION_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 270

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 279
class struct_anon_404(Structure):
    pass

struct_anon_404.__slots__ = [
    'id',
    'blob_type',
    'confidence',
    'reserved',
    'region',
    'privt_info',
]
struct_anon_404._fields_ = [
    ('id', c_uint),
    ('blob_type', c_uint),
    ('confidence', c_short),
    ('reserved', c_char * int(14)),
    ('region', VCA_REGION),
    ('privt_info', c_ubyte * int(40)),
]

HIK_TARGET_BLOB_EX = struct_anon_404# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 279

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 285
class struct__VCA_TARGET_LIST_V1_EX_(Structure):
    pass

struct__VCA_TARGET_LIST_V1_EX_.__slots__ = [
    'LineType',
    'target_num',
    'pstTarget',
]
struct__VCA_TARGET_LIST_V1_EX_._fields_ = [
    ('LineType', c_uint),
    ('target_num', c_uint),
    ('pstTarget', POINTER(HIK_TARGET_BLOB_EX)),
]

VCA_TARGET_LIST_V1_EX = struct__VCA_TARGET_LIST_V1_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 285

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 292
class struct__VCA_RULE_EX(Structure):
    pass

struct__VCA_RULE_EX.__slots__ = [
    'ID',
    'reserved',
    'polygon',
    'privt_info',
]
struct__VCA_RULE_EX._fields_ = [
    ('ID', c_ubyte),
    ('reserved', c_ubyte * int(15)),
    ('polygon', VCA_POLYGON_F),
    ('privt_info', c_ubyte * int(40)),
]

VCA_RULE_EX = struct__VCA_RULE_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 292

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 298
class struct__VCA_RULE_LIST_V3_EX_(Structure):
    pass

struct__VCA_RULE_LIST_V3_EX_.__slots__ = [
    'LineType',
    'rule_num',
    'pstRule',
]
struct__VCA_RULE_LIST_V3_EX_._fields_ = [
    ('LineType', c_uint),
    ('rule_num', c_uint),
    ('pstRule', POINTER(VCA_RULE_EX)),
]

VCA_RULE_LIST_V3_EX = struct__VCA_RULE_LIST_V3_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 298

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 306
class struct__VCA_ALERT_EX_(Structure):
    pass

struct__VCA_ALERT_EX_.__slots__ = [
    'alert',
    'reserved',
    'rule_info',
    'target',
    'privt_info',
]
struct__VCA_ALERT_EX_._fields_ = [
    ('alert', c_ubyte),
    ('reserved', c_ubyte * int(7)),
    ('rule_info', VCA_RULE_EX),
    ('target', VCA_TARGET_EX),
    ('privt_info', c_ubyte * int(40)),
]

VCA_ALERT_EX = struct__VCA_ALERT_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 306

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 311
class struct__VCA_ALERT_LIST_EX_(Structure):
    pass

struct__VCA_ALERT_LIST_EX_.__slots__ = [
    'alert_num',
    'pstAlert',
]
struct__VCA_ALERT_LIST_EX_._fields_ = [
    ('alert_num', c_uint),
    ('pstAlert', POINTER(VCA_ALERT_EX)),
]

VCA_ALERT_LIST_EX = struct__VCA_ALERT_LIST_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 311

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 320
class struct__PRIVATE_INFO_(Structure):
    pass

struct__PRIVATE_INFO_.__slots__ = [
    'type',
    'stTarget',
    'stTarget_EX',
    'stRule',
    'stRule_EX',
    'stAlert',
]
struct__PRIVATE_INFO_._fields_ = [
    ('type', c_uint),
    ('stTarget', VCA_TARGET_LIST_V1_EX),
    ('stTarget_EX', VCA_TARGET_LIST_V1_EX),
    ('stRule', VCA_RULE_LIST_V3_EX),
    ('stRule_EX', VCA_RULE_LIST_V3_EX),
    ('stAlert', VCA_ALERT_LIST_EX),
]

PRIVATE_INFO = struct__PRIVATE_INFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 320

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 336
class struct__HIK_MEDIAINFO_(Structure):
    pass

struct__HIK_MEDIAINFO_.__slots__ = [
    'media_fourcc',
    'media_version',
    'device_id',
    'system_format',
    'video_format',
    'audio_format',
    'audio_channels',
    'audio_bits_per_sample',
    'audio_samplesrate',
    'audio_bitrate',
    'reserved',
]
struct__HIK_MEDIAINFO_._fields_ = [
    ('media_fourcc', c_uint),
    ('media_version', c_ushort),
    ('device_id', c_ushort),
    ('system_format', c_ushort),
    ('video_format', c_ushort),
    ('audio_format', c_ushort),
    ('audio_channels', c_ubyte),
    ('audio_bits_per_sample', c_ubyte),
    ('audio_samplesrate', c_uint),
    ('audio_bitrate', c_uint),
    ('reserved', c_uint * int(4)),
]

HIK_MEDIAINFO = struct__HIK_MEDIAINFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 336

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 348
class struct_anon_405(Structure):
    pass

struct_anon_405.__slots__ = [
    'nPort',
    'pBuf',
    'nBufLen',
    'nWidth',
    'nHeight',
    'nStamp',
    'nType',
    'nUser',
]
struct_anon_405._fields_ = [
    ('nPort', c_long),
    ('pBuf', String),
    ('nBufLen', c_long),
    ('nWidth', c_long),
    ('nHeight', c_long),
    ('nStamp', c_long),
    ('nType', c_long),
    ('nUser', POINTER(None)),
]

DISPLAY_INFO = struct_anon_405# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 348

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 361
class struct_anon_406(Structure):
    pass

struct_anon_406.__slots__ = [
    'nPort',
    'pVideoBuf',
    'nVideoBufLen',
    'pPriBuf',
    'nPriBufLen',
    'nWidth',
    'nHeight',
    'nStamp',
    'nType',
    'nUser',
]
struct_anon_406._fields_ = [
    ('nPort', c_long),
    ('pVideoBuf', String),
    ('nVideoBufLen', c_long),
    ('pPriBuf', String),
    ('nPriBufLen', c_long),
    ('nWidth', c_long),
    ('nHeight', c_long),
    ('nStamp', c_long),
    ('nType', c_long),
    ('nUser', POINTER(None)),
]

DISPLAY_INFOEX = struct_anon_406# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 361

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 377
class struct_anon_407(Structure):
    pass

struct_anon_407.__slots__ = [
    'nPort',
    'pBuf',
    'nBufLen',
    'pBuf1',
    'nBufLen1',
    'pBuf2',
    'nBufLen2',
    'nWidth',
    'nHeight',
    'nStamp',
    'nType',
    'pUser',
    'reserved',
]
struct_anon_407._fields_ = [
    ('nPort', c_long),
    ('pBuf', String),
    ('nBufLen', c_uint),
    ('pBuf1', String),
    ('nBufLen1', c_uint),
    ('pBuf2', String),
    ('nBufLen2', c_uint),
    ('nWidth', c_uint),
    ('nHeight', c_uint),
    ('nStamp', c_uint),
    ('nType', c_uint),
    ('pUser', POINTER(None)),
    ('reserved', c_uint * int(4)),
]

DISPLAY_INFO_YUV = struct_anon_407# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 377

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 387
class struct_PLAYM4_SYSTEM_TIME(Structure):
    pass

struct_PLAYM4_SYSTEM_TIME.__slots__ = [
    'dwYear',
    'dwMon',
    'dwDay',
    'dwHour',
    'dwMin',
    'dwSec',
    'dwMs',
]
struct_PLAYM4_SYSTEM_TIME._fields_ = [
    ('dwYear', DWORD),
    ('dwMon', DWORD),
    ('dwDay', DWORD),
    ('dwHour', DWORD),
    ('dwMin', DWORD),
    ('dwSec', DWORD),
    ('dwMs', DWORD),
]

PLAYM4_SYSTEM_TIME = struct_PLAYM4_SYSTEM_TIME# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 387

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 399
class struct_anon_408(Structure):
    pass

struct_anon_408.__slots__ = [
    'pDataBuf',
    'dwPicSize',
    'dwBufSize',
    'dwPicWidth',
    'dwPicHeight',
    'dwReserve',
    'pCropRect',
]
struct_anon_408._fields_ = [
    ('pDataBuf', POINTER(BYTE)),
    ('dwPicSize', DWORD),
    ('dwBufSize', DWORD),
    ('dwPicWidth', DWORD),
    ('dwPicHeight', DWORD),
    ('dwReserve', DWORD),
    ('pCropRect', POINTER(RECT)),
]

CROP_PIC_INFO = struct_anon_408# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 399

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 406
class struct_anon_409(Structure):
    pass

struct_anon_409.__slots__ = [
    'nVideoEncryptType',
    'nAudioEncryptType',
    'nSetSecretKey',
]
struct_anon_409._fields_ = [
    ('nVideoEncryptType', c_long),
    ('nAudioEncryptType', c_long),
    ('nSetSecretKey', c_long),
]

ENCRYPT_INFO = struct_anon_409# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 406

enum__PLAYM4_PRIDATA_RENDER = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_ANA_INTEL_DATA = 0x00000001# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_MD = 0x00000002# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_ADD_POS = 0x00000004# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_ADD_PIC = 0x00000008# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_FIRE_DETCET = 0x00000010# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_TEM = 0x00000020# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_TRACK_TEM = 0x00000040# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_RENDER_THERMAL = 0x00000080# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

PLAYM4_PRIDATA_RENDER = enum__PLAYM4_PRIDATA_RENDER# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 417

enum__PLAYM4_THERMAL_FLAG = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 423

PLAYM4_THERMAL_FIREMASK = 0x00000001# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 423

PLAYM4_THERMAL_RULEGAS = 0x00000002# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 423

PLAYM4_THERMAL_TARGETGAS = 0x00000004# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 423

PLAYM4_THERMAL_FLAG = enum__PLAYM4_THERMAL_FLAG# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 423

enum__PLAYM4_FIRE_ALARM = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 430

PLAYM4_FIRE_FRAME_DIS = 0x00000001# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 430

PLAYM4_FIRE_MAX_TEMP = 0x00000002# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 430

PLAYM4_FIRE_MAX_TEMP_POSITION = 0x00000004# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 430

PLAYM4_FIRE_DISTANCE = 0x00000008# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 430

PLAYM4_FIRE_ALARM = enum__PLAYM4_FIRE_ALARM# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 430

enum__PLAYM4_TEM_FLAG = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 436

PLAYM4_TEM_REGION_BOX = 0x00000001# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 436

PLAYM4_TEM_REGION_LINE = 0x00000002# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 436

PLAYM4_TEM_REGION_POINT = 0x00000004# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 436

PLAYM4_TEM_FLAG = enum__PLAYM4_TEM_FLAG# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 436

enum__PLAYM4_TRACK_FLAG = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 441

PLAYM4_TRACK_PEOPLE = 0x00000001# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 441

PLAYM4_TRACK_VEHICLE = 0x00000002# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 441

PLAYM4_TRACK_FLAG = enum__PLAYM4_TRACK_FLAG# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 441

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 442
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPort", "cdecl"):
    PlayM4_GetPort = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPort", "cdecl")
    PlayM4_GetPort.argtypes = [POINTER(LONG)]
    PlayM4_GetPort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 443
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FreePort", "cdecl"):
    PlayM4_FreePort = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FreePort", "cdecl")
    PlayM4_FreePort.argtypes = [LONG]
    PlayM4_FreePort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 444
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_OpenFile", "cdecl"):
    PlayM4_OpenFile = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_OpenFile", "cdecl")
    PlayM4_OpenFile.argtypes = [LONG, LPSTR]
    PlayM4_OpenFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 445
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_CloseFile", "cdecl"):
    PlayM4_CloseFile = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_CloseFile", "cdecl")
    PlayM4_CloseFile.argtypes = [LONG]
    PlayM4_CloseFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 446
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_OpenStream", "cdecl"):
    PlayM4_OpenStream = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_OpenStream", "cdecl")
    PlayM4_OpenStream.argtypes = [LONG, PBYTE, DWORD, DWORD]
    PlayM4_OpenStream.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 447
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_CloseStream", "cdecl"):
    PlayM4_CloseStream = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_CloseStream", "cdecl")
    PlayM4_CloseStream.argtypes = [LONG]
    PlayM4_CloseStream.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 448
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_InputData", "cdecl"):
    PlayM4_InputData = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_InputData", "cdecl")
    PlayM4_InputData.argtypes = [LONG, PBYTE, DWORD]
    PlayM4_InputData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 449
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetStreamOpenMode", "cdecl"):
    PlayM4_SetStreamOpenMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetStreamOpenMode", "cdecl")
    PlayM4_SetStreamOpenMode.argtypes = [LONG, DWORD]
    PlayM4_SetStreamOpenMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 450
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetStreamOpenMode", "cdecl"):
    PlayM4_GetStreamOpenMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetStreamOpenMode", "cdecl")
    PlayM4_GetStreamOpenMode.argtypes = [LONG]
    PlayM4_GetStreamOpenMode.restype = LONG

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 451
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetFileRefCallBack", "cdecl"):
    PlayM4_SetFileRefCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetFileRefCallBack", "cdecl")
    PlayM4_SetFileRefCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), DWORD, POINTER(None)), POINTER(None)]
    PlayM4_SetFileRefCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 452
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetRefValue", "cdecl"):
    PlayM4_GetRefValue = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetRefValue", "cdecl")
    PlayM4_GetRefValue.argtypes = [LONG, POINTER(BYTE), POINTER(DWORD)]
    PlayM4_GetRefValue.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 453
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetRefValue", "cdecl"):
    PlayM4_SetRefValue = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetRefValue", "cdecl")
    PlayM4_SetRefValue.argtypes = [LONG, POINTER(BYTE), DWORD]
    PlayM4_SetRefValue.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 454
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetRefValueEx", "cdecl"):
    PlayM4_GetRefValueEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetRefValueEx", "cdecl")
    PlayM4_GetRefValueEx.argtypes = [LONG, POINTER(BYTE), POINTER(DWORD)]
    PlayM4_GetRefValueEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 455
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetKeyFramePos", "cdecl"):
    PlayM4_GetKeyFramePos = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetKeyFramePos", "cdecl")
    PlayM4_GetKeyFramePos.argtypes = [LONG, DWORD, DWORD, PFRAME_POS]
    PlayM4_GetKeyFramePos.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 456
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetNextKeyFramePos", "cdecl"):
    PlayM4_GetNextKeyFramePos = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetNextKeyFramePos", "cdecl")
    PlayM4_GetNextKeyFramePos.argtypes = [LONG, DWORD, DWORD, PFRAME_POS]
    PlayM4_GetNextKeyFramePos.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 457
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_Play", "cdecl"):
    PlayM4_Play = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_Play", "cdecl")
    PlayM4_Play.argtypes = [LONG, HWND]
    PlayM4_Play.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 458
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_Stop", "cdecl"):
    PlayM4_Stop = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_Stop", "cdecl")
    PlayM4_Stop.argtypes = [LONG]
    PlayM4_Stop.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 459
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_Pause", "cdecl"):
    PlayM4_Pause = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_Pause", "cdecl")
    PlayM4_Pause.argtypes = [LONG, DWORD]
    PlayM4_Pause.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 460
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_Fast", "cdecl"):
    PlayM4_Fast = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_Fast", "cdecl")
    PlayM4_Fast.argtypes = [LONG]
    PlayM4_Fast.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 461
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_Slow", "cdecl"):
    PlayM4_Slow = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_Slow", "cdecl")
    PlayM4_Slow.argtypes = [LONG]
    PlayM4_Slow.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 462
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_OneByOne", "cdecl"):
    PlayM4_OneByOne = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_OneByOne", "cdecl")
    PlayM4_OneByOne.argtypes = [LONG]
    PlayM4_OneByOne.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 463
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_OneByOneBack", "cdecl"):
    PlayM4_OneByOneBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_OneByOneBack", "cdecl")
    PlayM4_OneByOneBack.argtypes = [LONG]
    PlayM4_OneByOneBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 464
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ReversePlay", "cdecl"):
    PlayM4_ReversePlay = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ReversePlay", "cdecl")
    PlayM4_ReversePlay.argtypes = [LONG]
    PlayM4_ReversePlay.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 465
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RefreshPlay", "cdecl"):
    PlayM4_RefreshPlay = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RefreshPlay", "cdecl")
    PlayM4_RefreshPlay.argtypes = [LONG]
    PlayM4_RefreshPlay.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 466
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RefreshPlayEx", "cdecl"):
    PlayM4_RefreshPlayEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RefreshPlayEx", "cdecl")
    PlayM4_RefreshPlayEx.argtypes = [LONG, DWORD]
    PlayM4_RefreshPlayEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 467
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_PlaySound", "cdecl"):
    PlayM4_PlaySound = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_PlaySound", "cdecl")
    PlayM4_PlaySound.argtypes = [LONG]
    PlayM4_PlaySound.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 468
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_StopSound", "cdecl"):
    PlayM4_StopSound = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_StopSound", "cdecl")
    PlayM4_StopSound.argtypes = []
    PlayM4_StopSound.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 469
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_PlaySoundShare", "cdecl"):
    PlayM4_PlaySoundShare = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_PlaySoundShare", "cdecl")
    PlayM4_PlaySoundShare.argtypes = [LONG]
    PlayM4_PlaySoundShare.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 470
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_StopSoundShare", "cdecl"):
    PlayM4_StopSoundShare = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_StopSoundShare", "cdecl")
    PlayM4_StopSoundShare.argtypes = [LONG]
    PlayM4_StopSoundShare.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 471
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetVolume", "cdecl"):
    PlayM4_SetVolume = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetVolume", "cdecl")
    PlayM4_SetVolume.argtypes = [LONG, WORD]
    PlayM4_SetVolume.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 472
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetVolume", "cdecl"):
    PlayM4_GetVolume = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetVolume", "cdecl")
    PlayM4_GetVolume.argtypes = [LONG]
    PlayM4_GetVolume.restype = WORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 473
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_AdjustWaveAudio", "cdecl"):
    PlayM4_AdjustWaveAudio = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_AdjustWaveAudio", "cdecl")
    PlayM4_AdjustWaveAudio.argtypes = [LONG, LONG]
    PlayM4_AdjustWaveAudio.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 474
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetANRParam", "cdecl"):
    PlayM4_SetANRParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetANRParam", "cdecl")
    PlayM4_SetANRParam.argtypes = [LONG, BOOL, c_int]
    PlayM4_SetANRParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 475
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetPlayPos", "cdecl"):
    PlayM4_SetPlayPos = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetPlayPos", "cdecl")
    PlayM4_SetPlayPos.argtypes = [LONG, c_float]
    PlayM4_SetPlayPos.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 476
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPlayPos", "cdecl"):
    PlayM4_GetPlayPos = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPlayPos", "cdecl")
    PlayM4_GetPlayPos.argtypes = [LONG]
    PlayM4_GetPlayPos.restype = c_float

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 477
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetFileTime", "cdecl"):
    PlayM4_GetFileTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetFileTime", "cdecl")
    PlayM4_GetFileTime.argtypes = [LONG]
    PlayM4_GetFileTime.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 478
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPlayedTime", "cdecl"):
    PlayM4_GetPlayedTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPlayedTime", "cdecl")
    PlayM4_GetPlayedTime.argtypes = [LONG]
    PlayM4_GetPlayedTime.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 479
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPlayedFrames", "cdecl"):
    PlayM4_GetPlayedFrames = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPlayedFrames", "cdecl")
    PlayM4_GetPlayedFrames.argtypes = [LONG]
    PlayM4_GetPlayedFrames.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 480
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetFileTotalFrames", "cdecl"):
    PlayM4_GetFileTotalFrames = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetFileTotalFrames", "cdecl")
    PlayM4_GetFileTotalFrames.argtypes = [LONG]
    PlayM4_GetFileTotalFrames.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 481
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetCurrentFrameRate", "cdecl"):
    PlayM4_GetCurrentFrameRate = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetCurrentFrameRate", "cdecl")
    PlayM4_GetCurrentFrameRate.argtypes = [LONG]
    PlayM4_GetCurrentFrameRate.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 482
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPlayedTimeEx", "cdecl"):
    PlayM4_GetPlayedTimeEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPlayedTimeEx", "cdecl")
    PlayM4_GetPlayedTimeEx.argtypes = [LONG]
    PlayM4_GetPlayedTimeEx.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 483
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetPlayedTimeEx", "cdecl"):
    PlayM4_SetPlayedTimeEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetPlayedTimeEx", "cdecl")
    PlayM4_SetPlayedTimeEx.argtypes = [LONG, DWORD]
    PlayM4_SetPlayedTimeEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 484
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetCurrentFrameNum", "cdecl"):
    PlayM4_GetCurrentFrameNum = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetCurrentFrameNum", "cdecl")
    PlayM4_GetCurrentFrameNum.argtypes = [LONG]
    PlayM4_GetCurrentFrameNum.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 485
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetCurrentFrameNum", "cdecl"):
    PlayM4_SetCurrentFrameNum = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetCurrentFrameNum", "cdecl")
    PlayM4_SetCurrentFrameNum.argtypes = [LONG, DWORD]
    PlayM4_SetCurrentFrameNum.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 486
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetSystemTime", "cdecl"):
    PlayM4_GetSystemTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetSystemTime", "cdecl")
    PlayM4_GetSystemTime.argtypes = [LONG, POINTER(PLAYM4_SYSTEM_TIME)]
    PlayM4_GetSystemTime.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 487
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetSpecialData", "cdecl"):
    PlayM4_GetSpecialData = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetSpecialData", "cdecl")
    PlayM4_GetSpecialData.argtypes = [LONG]
    PlayM4_GetSpecialData.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 488
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPictureSize", "cdecl"):
    PlayM4_GetPictureSize = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPictureSize", "cdecl")
    PlayM4_GetPictureSize.argtypes = [LONG, POINTER(LONG), POINTER(LONG)]
    PlayM4_GetPictureSize.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 489
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetFileEndCallback", "cdecl"):
    PlayM4_SetFileEndCallback = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetFileEndCallback", "cdecl")
    PlayM4_SetFileEndCallback.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(None)), POINTER(None)]
    PlayM4_SetFileEndCallback.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 490
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetFileTotalTime", "cdecl"):
    PlayM4_GetFileTotalTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetFileTotalTime", "cdecl")
    PlayM4_GetFileTotalTime.argtypes = [LONG, POINTER(PLAYM4_SYSTEM_TIME), POINTER(PLAYM4_SYSTEM_TIME)]
    PlayM4_GetFileTotalTime.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 491
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetSupplementaryTimeZone", "cdecl"):
    PlayM4_SetSupplementaryTimeZone = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetSupplementaryTimeZone", "cdecl")
    PlayM4_SetSupplementaryTimeZone.argtypes = [c_int, c_int]
    PlayM4_SetSupplementaryTimeZone.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 492
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetSupplementaryTimeZone", "cdecl"):
    PlayM4_GetSupplementaryTimeZone = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetSupplementaryTimeZone", "cdecl")
    PlayM4_GetSupplementaryTimeZone.argtypes = [c_int, POINTER(c_int)]
    PlayM4_GetSupplementaryTimeZone.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 493
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetTimeZoneInfo", "cdecl"):
    PlayM4_GetTimeZoneInfo = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetTimeZoneInfo", "cdecl")
    PlayM4_GetTimeZoneInfo.argtypes = [c_long, POINTER(c_int)]
    PlayM4_GetTimeZoneInfo.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 494
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetStreamInfo", "cdecl"):
    PlayM4_GetStreamInfo = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetStreamInfo", "cdecl")
    PlayM4_GetStreamInfo.argtypes = [c_long, POINTER(c_int), POINTER(c_int)]
    PlayM4_GetStreamInfo.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 495
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetSourceBufferRemain", "cdecl"):
    PlayM4_GetSourceBufferRemain = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetSourceBufferRemain", "cdecl")
    PlayM4_GetSourceBufferRemain.argtypes = [LONG]
    PlayM4_GetSourceBufferRemain.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 496
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ResetSourceBuffer", "cdecl"):
    PlayM4_ResetSourceBuffer = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ResetSourceBuffer", "cdecl")
    PlayM4_ResetSourceBuffer.argtypes = [LONG]
    PlayM4_ResetSourceBuffer.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 497
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetSourceBufCallBack", "cdecl"):
    PlayM4_SetSourceBufCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetSourceBufCallBack", "cdecl")
    PlayM4_SetSourceBufCallBack.argtypes = [LONG, DWORD, CFUNCTYPE(UNCHECKED(None), c_long, DWORD, POINTER(None), POINTER(None)), POINTER(None), POINTER(None)]
    PlayM4_SetSourceBufCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 498
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ResetSourceBufFlag", "cdecl"):
    PlayM4_ResetSourceBufFlag = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ResetSourceBufFlag", "cdecl")
    PlayM4_ResetSourceBufFlag.argtypes = [LONG]
    PlayM4_ResetSourceBufFlag.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 499
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ResetBuffer", "cdecl"):
    PlayM4_ResetBuffer = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ResetBuffer", "cdecl")
    PlayM4_ResetBuffer.argtypes = [LONG, DWORD]
    PlayM4_ResetBuffer.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 500
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetBufferValue", "cdecl"):
    PlayM4_GetBufferValue = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetBufferValue", "cdecl")
    PlayM4_GetBufferValue.argtypes = [LONG, DWORD]
    PlayM4_GetBufferValue.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 501
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDisplayBuf", "cdecl"):
    PlayM4_SetDisplayBuf = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDisplayBuf", "cdecl")
    PlayM4_SetDisplayBuf.argtypes = [LONG, DWORD]
    PlayM4_SetDisplayBuf.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 502
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetDisplayBuf", "cdecl"):
    PlayM4_GetDisplayBuf = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetDisplayBuf", "cdecl")
    PlayM4_GetDisplayBuf.argtypes = [LONG]
    PlayM4_GetDisplayBuf.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 503
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetJpegQuality", "cdecl"):
    PlayM4_SetJpegQuality = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetJpegQuality", "cdecl")
    PlayM4_SetJpegQuality.argtypes = [c_long]
    PlayM4_SetJpegQuality.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 504
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetBMP", "cdecl"):
    PlayM4_GetBMP = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetBMP", "cdecl")
    PlayM4_GetBMP.argtypes = [LONG, PBYTE, DWORD, POINTER(DWORD)]
    PlayM4_GetBMP.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 505
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetJPEG", "cdecl"):
    PlayM4_GetJPEG = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetJPEG", "cdecl")
    PlayM4_GetJPEG.argtypes = [LONG, PBYTE, DWORD, POINTER(DWORD)]
    PlayM4_GetJPEG.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 506
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ConvertToBmpFile", "cdecl"):
    PlayM4_ConvertToBmpFile = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ConvertToBmpFile", "cdecl")
    PlayM4_ConvertToBmpFile.argtypes = [String, c_long, c_long, c_long, c_long, String]
    PlayM4_ConvertToBmpFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 507
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ConvertToJpegFile", "cdecl"):
    PlayM4_ConvertToJpegFile = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ConvertToJpegFile", "cdecl")
    PlayM4_ConvertToJpegFile.argtypes = [String, c_long, c_long, c_long, c_long, String]
    PlayM4_ConvertToJpegFile.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 508
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetIdemuxPara", "cdecl"):
    PlayM4_SetIdemuxPara = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetIdemuxPara", "cdecl")
    PlayM4_SetIdemuxPara.argtypes = [LONG, c_int]
    PlayM4_SetIdemuxPara.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 509
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetSecretKey", "cdecl"):
    PlayM4_SetSecretKey = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetSecretKey", "cdecl")
    PlayM4_SetSecretKey.argtypes = [LONG, LONG, String, LONG]
    PlayM4_SetSecretKey.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 510
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ThrowBFrameNum", "cdecl"):
    PlayM4_ThrowBFrameNum = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ThrowBFrameNum", "cdecl")
    PlayM4_ThrowBFrameNum.argtypes = [LONG, DWORD]
    PlayM4_ThrowBFrameNum.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 511
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecCBStream", "cdecl"):
    PlayM4_SetDecCBStream = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecCBStream", "cdecl")
    PlayM4_SetDecCBStream.argtypes = [LONG, DWORD]
    PlayM4_SetDecCBStream.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 512
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecodeFrameType", "cdecl"):
    PlayM4_SetDecodeFrameType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecodeFrameType", "cdecl")
    PlayM4_SetDecodeFrameType.argtypes = [LONG, DWORD]
    PlayM4_SetDecodeFrameType.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 513
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_CheckDiscontinuousFrameNum", "cdecl"):
    PlayM4_CheckDiscontinuousFrameNum = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_CheckDiscontinuousFrameNum", "cdecl")
    PlayM4_CheckDiscontinuousFrameNum.argtypes = [LONG, BOOL]
    PlayM4_CheckDiscontinuousFrameNum.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 514
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SkipErrorData", "cdecl"):
    PlayM4_SkipErrorData = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SkipErrorData", "cdecl")
    PlayM4_SkipErrorData.argtypes = [LONG, BOOL]
    PlayM4_SkipErrorData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 515
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecCallBackMend", "cdecl"):
    PlayM4_SetDecCallBackMend = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecCallBackMend", "cdecl")
    PlayM4_SetDecCallBackMend.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, String, c_long, POINTER(FRAME_INFO), POINTER(None), POINTER(None)), POINTER(None)]
    PlayM4_SetDecCallBackMend.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 516
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecCallBackExMend", "cdecl"):
    PlayM4_SetDecCallBackExMend = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecCallBackExMend", "cdecl")
    PlayM4_SetDecCallBackExMend.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, String, c_long, POINTER(FRAME_INFO), POINTER(None), POINTER(None)), String, c_long, POINTER(None)]
    PlayM4_SetDecCallBackExMend.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 517
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetEncryptTypeCallBack", "cdecl"):
    PlayM4_SetEncryptTypeCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetEncryptTypeCallBack", "cdecl")
    PlayM4_SetEncryptTypeCallBack.argtypes = [LONG, DWORD, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(ENCRYPT_INFO), POINTER(None), c_long), POINTER(None)]
    PlayM4_SetEncryptTypeCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 518
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecOrDisplayCallbackType", "cdecl"):
    PlayM4_SetDecOrDisplayCallbackType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecOrDisplayCallbackType", "cdecl")
    PlayM4_SetDecOrDisplayCallbackType.argtypes = [c_int, c_int, c_int]
    PlayM4_SetDecOrDisplayCallbackType.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 519
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDisplayRegion", "cdecl"):
    PlayM4_SetDisplayRegion = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDisplayRegion", "cdecl")
    PlayM4_SetDisplayRegion.argtypes = [LONG, DWORD, POINTER(RECT), HWND, BOOL]
    PlayM4_SetDisplayRegion.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 520
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDisplayRegionOnWnd", "cdecl"):
    PlayM4_SetDisplayRegionOnWnd = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDisplayRegionOnWnd", "cdecl")
    PlayM4_SetDisplayRegionOnWnd.argtypes = [LONG, DWORD, POINTER(RECT), BOOL]
    PlayM4_SetDisplayRegionOnWnd.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 521
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDisplayType", "cdecl"):
    PlayM4_SetDisplayType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDisplayType", "cdecl")
    PlayM4_SetDisplayType.argtypes = [LONG, LONG]
    PlayM4_SetDisplayType.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 522
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetDisplayType", "cdecl"):
    PlayM4_GetDisplayType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetDisplayType", "cdecl")
    PlayM4_GetDisplayType.argtypes = [LONG]
    PlayM4_GetDisplayType.restype = c_long

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 523
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDisplayCallBack", "cdecl"):
    PlayM4_SetDisplayCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDisplayCallBack", "cdecl")
    PlayM4_SetDisplayCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, String, c_long, c_long, c_long, c_long, c_long, POINTER(None))]
    PlayM4_SetDisplayCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 524
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDisplayCallBackEx", "cdecl"):
    PlayM4_SetDisplayCallBackEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDisplayCallBackEx", "cdecl")
    PlayM4_SetDisplayCallBackEx.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), POINTER(DISPLAY_INFO)), POINTER(None)]
    PlayM4_SetDisplayCallBackEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 525
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RegisterDrawFun", "cdecl"):
    PlayM4_RegisterDrawFun = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RegisterDrawFun", "cdecl")
    PlayM4_RegisterDrawFun.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, HDC, POINTER(None)), POINTER(None)]
    PlayM4_RegisterDrawFun.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 526
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetEncTypeChangeCallBack", "cdecl"):
    PlayM4_SetEncTypeChangeCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetEncTypeChangeCallBack", "cdecl")
    PlayM4_SetEncTypeChangeCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(None)), POINTER(None)]
    PlayM4_SetEncTypeChangeCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 527
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetCheckWatermarkCallBack", "cdecl"):
    PlayM4_SetCheckWatermarkCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetCheckWatermarkCallBack", "cdecl")
    PlayM4_SetCheckWatermarkCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(WATERMARK_INFO), POINTER(None)), POINTER(None)]
    PlayM4_SetCheckWatermarkCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 528
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RenderPrivateData", "cdecl"):
    PlayM4_RenderPrivateData = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RenderPrivateData", "cdecl")
    PlayM4_RenderPrivateData.argtypes = [LONG, c_int, BOOL]
    PlayM4_RenderPrivateData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 529
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RenderPrivateDataEx", "cdecl"):
    PlayM4_RenderPrivateDataEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RenderPrivateDataEx", "cdecl")
    PlayM4_RenderPrivateDataEx.argtypes = [LONG, c_int, c_int, BOOL]
    PlayM4_RenderPrivateDataEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 530
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetOverlayPriInfoFlag", "cdecl"):
    PlayM4_SetOverlayPriInfoFlag = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetOverlayPriInfoFlag", "cdecl")
    PlayM4_SetOverlayPriInfoFlag.argtypes = [LONG, c_int, BOOL]
    PlayM4_SetOverlayPriInfoFlag.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 531
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetTrackDurationTime", "cdecl"):
    PlayM4_SetTrackDurationTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetTrackDurationTime", "cdecl")
    PlayM4_SetTrackDurationTime.argtypes = [LONG, c_int]
    PlayM4_SetTrackDurationTime.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 532
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RegisterIVSDrawFunCB_EX", "cdecl"):
    PlayM4_RegisterIVSDrawFunCB_EX = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RegisterIVSDrawFunCB_EX", "cdecl")
    PlayM4_RegisterIVSDrawFunCB_EX.argtypes = [c_long, CFUNCTYPE(UNCHECKED(None), c_long, HDC, POINTER(FRAME_INFO), POINTER(INTEL_INFO_EX), POINTER(None)), POINTER(None), c_uint]
    PlayM4_RegisterIVSDrawFunCB_EX.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 533
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetStreamAdditionalInfo", "cdecl"):
    PlayM4_GetStreamAdditionalInfo = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetStreamAdditionalInfo", "cdecl")
    PlayM4_GetStreamAdditionalInfo.argtypes = [LONG, LONG, POINTER(BYTE), POINTER(LONG)]
    PlayM4_GetStreamAdditionalInfo.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 534
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetColor", "cdecl"):
    PlayM4_SetColor = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetColor", "cdecl")
    PlayM4_SetColor.argtypes = [LONG, DWORD, c_int, c_int, c_int, c_int]
    PlayM4_SetColor.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 535
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetColor", "cdecl"):
    PlayM4_GetColor = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetColor", "cdecl")
    PlayM4_GetColor.argtypes = [LONG, DWORD, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    PlayM4_GetColor.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 536
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetImageSharpen", "cdecl"):
    PlayM4_SetImageSharpen = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetImageSharpen", "cdecl")
    PlayM4_SetImageSharpen.argtypes = [LONG, DWORD]
    PlayM4_SetImageSharpen.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 537
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetRotateAngle", "cdecl"):
    PlayM4_SetRotateAngle = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetRotateAngle", "cdecl")
    PlayM4_SetRotateAngle.argtypes = [LONG, DWORD, DWORD]
    PlayM4_SetRotateAngle.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 538
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetFileHeadLength", "cdecl"):
    PlayM4_GetFileHeadLength = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetFileHeadLength", "cdecl")
    PlayM4_GetFileHeadLength.argtypes = []
    PlayM4_GetFileHeadLength.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 539
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetSdkVersion", "cdecl"):
    PlayM4_GetSdkVersion = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetSdkVersion", "cdecl")
    PlayM4_GetSdkVersion.argtypes = []
    PlayM4_GetSdkVersion.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 540
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetLastError", "cdecl"):
    PlayM4_GetLastError = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetLastError", "cdecl")
    PlayM4_GetLastError.argtypes = [LONG]
    PlayM4_GetLastError.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 541
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetSycGroup", "cdecl"):
    PlayM4_SetSycGroup = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetSycGroup", "cdecl")
    PlayM4_SetSycGroup.argtypes = [LONG, DWORD]
    PlayM4_SetSycGroup.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 542
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_MotionFlow", "cdecl"):
    PlayM4_MotionFlow = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_MotionFlow", "cdecl")
    PlayM4_MotionFlow.argtypes = [LONG, DWORD]
    PlayM4_MotionFlow.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 543
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RegisterIVSIntelInfoCB", "cdecl"):
    PlayM4_RegisterIVSIntelInfoCB = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RegisterIVSIntelInfoCB", "cdecl")
    PlayM4_RegisterIVSIntelInfoCB.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), LONG, HDC, LONG, POINTER(PRIVATE_INFO), POINTER(None)), POINTER(None), DWORD, DWORD]
    PlayM4_RegisterIVSIntelInfoCB.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 544
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetMpOffset", "cdecl"):
    PlayM4_GetMpOffset = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetMpOffset", "cdecl")
    PlayM4_GetMpOffset.argtypes = [c_int, c_int, POINTER(c_int)]
    PlayM4_GetMpOffset.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 545
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetHLogFlag", "cdecl"):
    PlayM4_SetHLogFlag = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetHLogFlag", "cdecl")
    PlayM4_SetHLogFlag.argtypes = [c_int, BOOL, String]
    PlayM4_SetHLogFlag.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 569
class struct__tagHDECODESUPPORT_(Structure):
    pass

struct__tagHDECODESUPPORT_.__slots__ = [
    'chGPUType',
    'bDXVA_D3D9',
    'bCUVID_D3D11',
    'chDXVAH264_Max_Resolution',
    'chDXVAH265_Max_Resolution',
    'chCUVIDH264_Max_Resolution',
    'chCUVIDH265_Max_Resolution',
    'chValidFlag',
    'bD3D11VA',
    'chD3D11VAH264_Max_Resolution',
    'chD3D11VAH265_Max_Resolution',
    'nReserved',
]
struct__tagHDECODESUPPORT_._fields_ = [
    ('chGPUType', c_ubyte),
    ('bDXVA_D3D9', c_ubyte),
    ('bCUVID_D3D11', c_ubyte),
    ('chDXVAH264_Max_Resolution', c_ubyte),
    ('chDXVAH265_Max_Resolution', c_ubyte),
    ('chCUVIDH264_Max_Resolution', c_ubyte),
    ('chCUVIDH265_Max_Resolution', c_ubyte),
    ('chValidFlag', c_ubyte),
    ('bD3D11VA', c_ubyte),
    ('chD3D11VAH264_Max_Resolution', c_ubyte),
    ('chD3D11VAH265_Max_Resolution', c_ubyte),
    ('nReserved', c_ubyte * int(9)),
]

HDECODESUPPORT = struct__tagHDECODESUPPORT_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 569

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 579
class struct__tagRENDERSUPPORT_(Structure):
    pass

struct__tagRENDERSUPPORT_.__slots__ = [
    'bDDraw',
    'bD3D9Surface',
    'bD3D9Texture',
    'bD3D11',
    'chValidFlag',
    'nGPUType',
    'nReserved',
]
struct__tagRENDERSUPPORT_._fields_ = [
    ('bDDraw', c_ubyte),
    ('bD3D9Surface', c_ubyte),
    ('bD3D9Texture', c_ubyte),
    ('bD3D11', c_ubyte),
    ('chValidFlag', c_ubyte),
    ('nGPUType', c_ubyte),
    ('nReserved', c_ubyte * int(10)),
]

RENDERSUPPORT = struct__tagRENDERSUPPORT_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 579

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 585
class struct__tagENGINESUPPORT_(Structure):
    pass

struct__tagENGINESUPPORT_.__slots__ = [
    'stHDecodeSupport',
    'stRenderSupport',
    'chReserved',
]
struct__tagENGINESUPPORT_._fields_ = [
    ('stHDecodeSupport', HDECODESUPPORT),
    ('stRenderSupport', RENDERSUPPORT),
    ('chReserved', c_uint * int(4)),
]

ENGINESUPPORT = struct__tagENGINESUPPORT_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 585

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 595
class struct__tagENGINESUPPORT_EX_(Structure):
    pass

struct__tagENGINESUPPORT_EX_.__slots__ = [
    'stHDecodeSupportD3D9',
    'stHDecodeSupportD3D11',
    'stRenderSupport',
    'chD3D9DeviceCount',
    'chD3D11DeviceCount',
    'chRenderDeviceCount',
    'chReserved',
]
struct__tagENGINESUPPORT_EX_._fields_ = [
    ('stHDecodeSupportD3D9', HDECODESUPPORT * int(8)),
    ('stHDecodeSupportD3D11', HDECODESUPPORT * int(8)),
    ('stRenderSupport', RENDERSUPPORT * int(8)),
    ('chD3D9DeviceCount', c_ubyte),
    ('chD3D11DeviceCount', c_ubyte),
    ('chRenderDeviceCount', c_ubyte),
    ('chReserved', c_ubyte * int(13)),
]

ENGINESUPPORT_EX = struct__tagENGINESUPPORT_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 595

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 605
class struct__tagD3D11_PIC_INFO_(Structure):
    pass

struct__tagD3D11_PIC_INFO_.__slots__ = [
    'nPicMode',
    'pBuf',
    'nBufSize',
    'pPicSize',
    'nPicWidth',
    'nPicHeight',
    'chReserve',
]
struct__tagD3D11_PIC_INFO_._fields_ = [
    ('nPicMode', c_uint),
    ('pBuf', POINTER(c_ubyte)),
    ('nBufSize', c_uint),
    ('pPicSize', POINTER(c_uint)),
    ('nPicWidth', c_uint),
    ('nPicHeight', c_uint),
    ('chReserve', c_ubyte * int(8)),
]

D3D_PIC_INFO = struct__tagD3D11_PIC_INFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 605

enum_tagPLAYM4PostProcType = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

PLAYM4_PPT_BRIGHTNESS = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

PLAYM4_PPT_HUE = 0x2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

PLAYM4_PPT_SATURATION = 0x3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

PLAYM4_PPT_CONTRAST = 0x4# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

PLAYM4_PPT_SHARPNESS = 0x5# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

PLAYM4PostProcType = enum_tagPLAYM4PostProcType# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 613

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 615
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetEngineSupport", "cdecl"):
    PlayM4_GetEngineSupport = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetEngineSupport", "cdecl")
    PlayM4_GetEngineSupport.argtypes = [c_long, POINTER(ENGINESUPPORT)]
    PlayM4_GetEngineSupport.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 616
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetD3DCapture", "cdecl"):
    PlayM4_GetD3DCapture = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetD3DCapture", "cdecl")
    PlayM4_GetD3DCapture.argtypes = [c_long, c_uint, POINTER(D3D_PIC_INFO)]
    PlayM4_GetD3DCapture.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 617
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetD3DPostProcess", "cdecl"):
    PlayM4_SetD3DPostProcess = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetD3DPostProcess", "cdecl")
    PlayM4_SetD3DPostProcess.argtypes = [c_long, PLAYM4PostProcType, c_float]
    PlayM4_SetD3DPostProcess.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 618
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetD3DPostProcess", "cdecl"):
    PlayM4_GetD3DPostProcess = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetD3DPostProcess", "cdecl")
    PlayM4_GetD3DPostProcess.argtypes = [c_long, PLAYM4PostProcType, POINTER(c_float)]
    PlayM4_GetD3DPostProcess.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 619
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetConfigFontPath", "cdecl"):
    PlayM4_SetConfigFontPath = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetConfigFontPath", "cdecl")
    PlayM4_SetConfigFontPath.argtypes = [c_int, String]
    PlayM4_SetConfigFontPath.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 629
class struct__PLAYM4_SESSION_INFO_(Structure):
    pass

struct__PLAYM4_SESSION_INFO_.__slots__ = [
    'nSessionInfoType',
    'nSessionInfoLen',
    'pSessionInfoData',
]
struct__PLAYM4_SESSION_INFO_._fields_ = [
    ('nSessionInfoType', c_int),
    ('nSessionInfoLen', c_int),
    ('pSessionInfoData', POINTER(c_ubyte)),
]

PLAYM4_SESSION_INFO = struct__PLAYM4_SESSION_INFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 629

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 631
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_OpenStreamAdvanced", "cdecl"):
    PlayM4_OpenStreamAdvanced = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_OpenStreamAdvanced", "cdecl")
    PlayM4_OpenStreamAdvanced.argtypes = [LONG, c_int, POINTER(PLAYM4_SESSION_INFO), DWORD]
    PlayM4_OpenStreamAdvanced.restype = BOOL

enum_tagFECPlaceType = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 639

FEC_PLACE_WALL = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 639

FEC_PLACE_FLOOR = 0x2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 639

FEC_PLACE_CEILING = 0x3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 639

FECPLACETYPE = enum_tagFECPlaceType# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 639

enum_tagFECCorrectType = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_NULL = 0x0000# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_PTZ = 0x0100# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_180 = 0x0200# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_360 = 0x0300# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_LAT = 0x0400# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_SEMISPHERE = 0x0500# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_CYLINDER = 0x0600# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_CYLINDER_SPLIT = 0x0700# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_PLANET = 0x0800# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_ARCSPHERE_HORIZONTAL = 0x0900# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FEC_CORRECT_ARCSPHERE_VERTICAL = 0x0A00# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

FECCORRECTTYPE = enum_tagFECCorrectType# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 653

enum_tagFECCorrectEffect = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 657

FEC_CORRECT_EFFECT_BACK_FACE_CULLING = 0x100# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 657

FECCORRECTEFFECT = enum_tagFECCorrectEffect# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 657

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 664
class struct_tagCycleParam(Structure):
    pass

struct_tagCycleParam.__slots__ = [
    'fRadiusLeft',
    'fRadiusRight',
    'fRadiusTop',
    'fRadiusBottom',
]
struct_tagCycleParam._fields_ = [
    ('fRadiusLeft', c_float),
    ('fRadiusRight', c_float),
    ('fRadiusTop', c_float),
    ('fRadiusBottom', c_float),
]

CYCLEPARAM = struct_tagCycleParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 664

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 669
class struct_tagPTZParam(Structure):
    pass

struct_tagPTZParam.__slots__ = [
    'fPTZPositionX',
    'fPTZPositionY',
]
struct_tagPTZParam._fields_ = [
    ('fPTZPositionX', c_float),
    ('fPTZPositionY', c_float),
]

PTZPARAM = struct_tagPTZParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 669

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 682
class struct_tagFECColor(Structure):
    pass

struct_tagFECColor.__slots__ = [
    'nR',
    'nG',
    'nB',
    'nAlpha',
]
struct_tagFECColor._fields_ = [
    ('nR', c_ubyte),
    ('nG', c_ubyte),
    ('nB', c_ubyte),
    ('nAlpha', c_ubyte),
]

FECCOLOR = struct_tagFECColor# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 682

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 689
class struct_tagFECRectF(Structure):
    pass

struct_tagFECRectF.__slots__ = [
    'fTop',
    'fBottom',
    'fLeft',
    'fRight',
]
struct_tagFECRectF._fields_ = [
    ('fTop', c_float),
    ('fBottom', c_float),
    ('fLeft', c_float),
    ('fRight', c_float),
]

FECRECTF = struct_tagFECRectF# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 689

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 702
class struct_tagFECParam(Structure):
    pass

struct_tagFECParam.__slots__ = [
    'nUpDateType',
    'nPlaceAndCorrect',
    'stPTZParam',
    'stCycleParam',
    'fZoom',
    'fWideScanOffset',
    'stPTZColor',
    'stPTZSelct',
    'nCut',
    'nResver',
]
struct_tagFECParam._fields_ = [
    ('nUpDateType', c_uint),
    ('nPlaceAndCorrect', c_uint),
    ('stPTZParam', PTZPARAM),
    ('stCycleParam', CYCLEPARAM),
    ('fZoom', c_float),
    ('fWideScanOffset', c_float),
    ('stPTZColor', FECCOLOR),
    ('stPTZSelct', FECRECTF),
    ('nCut', c_uint),
    ('nResver', c_int * int(10)),
]

FISHEYEPARAM = struct_tagFECParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 702

enum_tagFECShowMode = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 708

FEC_PTZ_OUTLINE_NULL = 0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 708

FEC_PTZ_OUTLINE_RECT = (FEC_PTZ_OUTLINE_NULL + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 708

FEC_PTZ_OUTLINE_RANGE = (FEC_PTZ_OUTLINE_RECT + 1)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 708

FECSHOWMODE = enum_tagFECShowMode# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 708

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 718
class struct_tagPLAYM4SRTransformElement(Structure):
    pass

struct_tagPLAYM4SRTransformElement.__slots__ = [
    'fAxisX',
    'fAxisY',
    'fAxisZ',
    'fValue',
]
struct_tagPLAYM4SRTransformElement._fields_ = [
    ('fAxisX', c_float),
    ('fAxisY', c_float),
    ('fAxisZ', c_float),
    ('fValue', c_float),
]

PLAYM4SRTRANSFERELEMENT = struct_tagPLAYM4SRTransformElement# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 718

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 723
class struct_tagPLAYM4SRTransformParam(Structure):
    pass

struct_tagPLAYM4SRTransformParam.__slots__ = [
    'pTransformElement',
    'nTransformCount',
]
struct_tagPLAYM4SRTransformParam._fields_ = [
    ('pTransformElement', POINTER(PLAYM4SRTRANSFERELEMENT)),
    ('nTransformCount', c_uint),
]

PLAYM4SRTRANSFERPARAM = struct_tagPLAYM4SRTransformParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 723

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 725
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_Rotate", "cdecl"):
    PlayM4_FEC_Rotate = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_Rotate", "cdecl")
    PlayM4_FEC_Rotate.argtypes = [LONG, POINTER(PLAYM4SRTRANSFERPARAM)]
    PlayM4_FEC_Rotate.restype = BOOL

enum_tagPLAYM4HRViewParamType = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 731

PLAYM4_HR_VPT_ROTATION_X = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 731

PLAYM4_HR_VPT_ROTATION_Y = 0x2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 731

PLAYM4_HR_VPT_SCALE = 0x3# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 731

PLAYM4HRVIEWPARAMTYPE = enum_tagPLAYM4HRViewParamType# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 731

enum_tagPLAYM4FEC3DModelParam = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 736

PLAYM4_FEC_3DMP_CYLINDER_HEIGHT = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 736

PLAYM4_FEC_3DMP_CYLINDER_RADIUS = 0x2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 736

PLAYM4FEC3DMODELPARAM = enum_tagPLAYM4FEC3DModelParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 736

enum_tagPLAYM4FECSpecialViewType = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 740

PLAYM4_FEC_SVT_EDGE = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 740

PLAYM4FECSPECIALVIEWTYPE = enum_tagPLAYM4FECSpecialViewType# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 740

FISHEYE_CallBack = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_uint, c_uint, POINTER(None), c_uint, c_uint)# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 741

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 743
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_Enable", "cdecl"):
    PlayM4_FEC_Enable = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_Enable", "cdecl")
    PlayM4_FEC_Enable.argtypes = [LONG]
    PlayM4_FEC_Enable.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 744
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_Disable", "cdecl"):
    PlayM4_FEC_Disable = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_Disable", "cdecl")
    PlayM4_FEC_Disable.argtypes = [LONG]
    PlayM4_FEC_Disable.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 745
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_GetPort", "cdecl"):
    PlayM4_FEC_GetPort = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_GetPort", "cdecl")
    PlayM4_FEC_GetPort.argtypes = [LONG, POINTER(c_uint), FECPLACETYPE, FECCORRECTTYPE]
    PlayM4_FEC_GetPort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 746
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_DelPort", "cdecl"):
    PlayM4_FEC_DelPort = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_DelPort", "cdecl")
    PlayM4_FEC_DelPort.argtypes = [LONG, c_uint]
    PlayM4_FEC_DelPort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 747
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetParam", "cdecl"):
    PlayM4_FEC_SetParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetParam", "cdecl")
    PlayM4_FEC_SetParam.argtypes = [LONG, c_uint, POINTER(FISHEYEPARAM)]
    PlayM4_FEC_SetParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 748
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_GetParam", "cdecl"):
    PlayM4_FEC_GetParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_GetParam", "cdecl")
    PlayM4_FEC_GetParam.argtypes = [LONG, c_uint, POINTER(FISHEYEPARAM)]
    PlayM4_FEC_GetParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 749
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetWnd", "cdecl"):
    PlayM4_FEC_SetWnd = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetWnd", "cdecl")
    PlayM4_FEC_SetWnd.argtypes = [LONG, c_uint, POINTER(None)]
    PlayM4_FEC_SetWnd.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 750
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetCallBack", "cdecl"):
    PlayM4_FEC_SetCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetCallBack", "cdecl")
    PlayM4_FEC_SetCallBack.argtypes = [LONG, c_uint, FISHEYE_CallBack, POINTER(None)]
    PlayM4_FEC_SetCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 751
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_Capture", "cdecl"):
    PlayM4_FEC_Capture = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_Capture", "cdecl")
    PlayM4_FEC_Capture.argtypes = [LONG, c_uint, c_uint, String]
    PlayM4_FEC_Capture.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 752
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetConfig", "cdecl"):
    PlayM4_FEC_SetConfig = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetConfig", "cdecl")
    PlayM4_FEC_SetConfig.argtypes = [LONG, c_uint]
    PlayM4_FEC_SetConfig.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 753
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_GetCurrentPTZPort", "cdecl"):
    PlayM4_FEC_GetCurrentPTZPort = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_GetCurrentPTZPort", "cdecl")
    PlayM4_FEC_GetCurrentPTZPort.argtypes = [LONG, c_float, c_float, POINTER(c_uint)]
    PlayM4_FEC_GetCurrentPTZPort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 754
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetCurrentPTZPort", "cdecl"):
    PlayM4_FEC_SetCurrentPTZPort = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetCurrentPTZPort", "cdecl")
    PlayM4_FEC_SetCurrentPTZPort.argtypes = [LONG, c_uint]
    PlayM4_FEC_SetCurrentPTZPort.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 755
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetPTZOutLineShowMode", "cdecl"):
    PlayM4_FEC_SetPTZOutLineShowMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetPTZOutLineShowMode", "cdecl")
    PlayM4_FEC_SetPTZOutLineShowMode.argtypes = [LONG, FECSHOWMODE]
    PlayM4_FEC_SetPTZOutLineShowMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 756
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_GetViewParam", "cdecl"):
    PlayM4_FEC_GetViewParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_GetViewParam", "cdecl")
    PlayM4_FEC_GetViewParam.argtypes = [LONG, c_uint, PLAYM4HRVIEWPARAMTYPE, POINTER(c_float)]
    PlayM4_FEC_GetViewParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 757
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetViewParam", "cdecl"):
    PlayM4_FEC_SetViewParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetViewParam", "cdecl")
    PlayM4_FEC_SetViewParam.argtypes = [LONG, c_uint, PLAYM4HRVIEWPARAMTYPE, c_float]
    PlayM4_FEC_SetViewParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 758
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetDisplayRegion", "cdecl"):
    PlayM4_FEC_SetDisplayRegion = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetDisplayRegion", "cdecl")
    PlayM4_FEC_SetDisplayRegion.argtypes = [LONG, c_uint, c_uint, DWORD, POINTER(RECT), HWND, BOOL]
    PlayM4_FEC_SetDisplayRegion.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 759
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_SetCorrectEffect", "cdecl"):
    PlayM4_FEC_SetCorrectEffect = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_SetCorrectEffect", "cdecl")
    PlayM4_FEC_SetCorrectEffect.argtypes = [LONG, c_uint, FECCORRECTEFFECT, c_float]
    PlayM4_FEC_SetCorrectEffect.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 760
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_Set3DModelParam", "cdecl"):
    PlayM4_FEC_Set3DModelParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_Set3DModelParam", "cdecl")
    PlayM4_FEC_Set3DModelParam.argtypes = [c_int, c_uint, PLAYM4FEC3DMODELPARAM, c_float]
    PlayM4_FEC_Set3DModelParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 761
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_FEC_GetSpecialViewParam", "cdecl"):
    PlayM4_FEC_GetSpecialViewParam = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_FEC_GetSpecialViewParam", "cdecl")
    PlayM4_FEC_GetSpecialViewParam.argtypes = [c_int, c_uint, PLAYM4FECSPECIALVIEWTYPE, PLAYM4HRVIEWPARAMTYPE, POINTER(c_float)]
    PlayM4_FEC_GetSpecialViewParam.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 784
class struct__PLAYM4_VIE_DYNPARAM_(Structure):
    pass

struct__PLAYM4_VIE_DYNPARAM_.__slots__ = [
    'moduFlag',
    'brightVal',
    'contrastVal',
    'colorVal',
    'toneScale',
    'toneGain',
    'toneOffset',
    'toneColor',
    'dehazeLevel',
    'dehazeTrans',
    'dehazeBright',
    'denoiseLevel',
    'usmAmount',
    'usmRadius',
    'usmThreshold',
    'deblockLevel',
    'lensWarp',
    'lensZoom',
]
struct__PLAYM4_VIE_DYNPARAM_._fields_ = [
    ('moduFlag', c_int),
    ('brightVal', c_int),
    ('contrastVal', c_int),
    ('colorVal', c_int),
    ('toneScale', c_int),
    ('toneGain', c_int),
    ('toneOffset', c_int),
    ('toneColor', c_int),
    ('dehazeLevel', c_int),
    ('dehazeTrans', c_int),
    ('dehazeBright', c_int),
    ('denoiseLevel', c_int),
    ('usmAmount', c_int),
    ('usmRadius', c_int),
    ('usmThreshold', c_int),
    ('deblockLevel', c_int),
    ('lensWarp', c_int),
    ('lensZoom', c_int),
]

PLAYM4_VIE_PARACONFIG = struct__PLAYM4_VIE_DYNPARAM_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 784

enum__PLAYM4_VIE_MODULES = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_ADJ = 0x00000001# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_EHAN = 0x00000002# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_DEHAZE = 0x00000004# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_DENOISE = 0x00000008# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_SHARPEN = 0x00000010# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_DEBLOCK = 0x00000020# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_CRB = 0x00000040# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODU_LENS = 0x00000080# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

PLAYM4_VIE_MODULES = enum__PLAYM4_VIE_MODULES# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 795

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 797
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_VIE_SetModuConfig", "cdecl"):
    PlayM4_VIE_SetModuConfig = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_VIE_SetModuConfig", "cdecl")
    PlayM4_VIE_SetModuConfig.argtypes = [LONG, c_int, BOOL]
    PlayM4_VIE_SetModuConfig.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 798
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_VIE_SetRegion", "cdecl"):
    PlayM4_VIE_SetRegion = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_VIE_SetRegion", "cdecl")
    PlayM4_VIE_SetRegion.argtypes = [LONG, LONG, POINTER(RECT)]
    PlayM4_VIE_SetRegion.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 799
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_VIE_GetModuConfig", "cdecl"):
    PlayM4_VIE_GetModuConfig = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_VIE_GetModuConfig", "cdecl")
    PlayM4_VIE_GetModuConfig.argtypes = [LONG, POINTER(c_int)]
    PlayM4_VIE_GetModuConfig.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 800
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_VIE_SetParaConfig", "cdecl"):
    PlayM4_VIE_SetParaConfig = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_VIE_SetParaConfig", "cdecl")
    PlayM4_VIE_SetParaConfig.argtypes = [LONG, POINTER(PLAYM4_VIE_PARACONFIG)]
    PlayM4_VIE_SetParaConfig.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 801
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_VIE_GetParaConfig", "cdecl"):
    PlayM4_VIE_GetParaConfig = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_VIE_GetParaConfig", "cdecl")
    PlayM4_VIE_GetParaConfig.argtypes = [LONG, POINTER(PLAYM4_VIE_PARACONFIG)]
    PlayM4_VIE_GetParaConfig.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 809
class struct_anon_410(Structure):
    pass

struct_anon_410.__slots__ = [
    'lDataType',
    'lDataStrVersion',
    'lDataTimeStamp',
    'lDataLength',
    'pData',
]
struct_anon_410._fields_ = [
    ('lDataType', c_long),
    ('lDataStrVersion', c_long),
    ('lDataTimeStamp', c_long),
    ('lDataLength', c_long),
    ('pData', String),
]

AdditionDataInfo = struct_anon_410# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 809

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 810
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetAdditionDataCallBack", "cdecl"):
    PlayM4_SetAdditionDataCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetAdditionDataCallBack", "cdecl")
    PlayM4_SetAdditionDataCallBack.argtypes = [LONG, DWORD, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(AdditionDataInfo), POINTER(None)), POINTER(None)]
    PlayM4_SetAdditionDataCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 813
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecodeEngineEx", "cdecl"):
    PlayM4_SetDecodeEngineEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecodeEngineEx", "cdecl")
    PlayM4_SetDecodeEngineEx.argtypes = [LONG, DWORD]
    PlayM4_SetDecodeEngineEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 814
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetDecodeEngine", "cdecl"):
    PlayM4_GetDecodeEngine = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetDecodeEngine", "cdecl")
    PlayM4_GetDecodeEngine.argtypes = [LONG]
    PlayM4_GetDecodeEngine.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 848
class struct_anon_411(Structure):
    pass

struct_anon_411.__slots__ = [
    'nRunTimeModule',
    'nStrVersion',
    'nFrameTimeStamp',
    'nFrameNum',
    'nErrorCode',
    'reserved',
]
struct_anon_411._fields_ = [
    ('nRunTimeModule', c_int),
    ('nStrVersion', c_int),
    ('nFrameTimeStamp', c_int),
    ('nFrameNum', c_int),
    ('nErrorCode', c_int),
    ('reserved', c_ubyte * int(12)),
]

RunTimeInfo = struct_anon_411# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 848

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 849
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetRunTimeInfoCallBackEx", "cdecl"):
    PlayM4_SetRunTimeInfoCallBackEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetRunTimeInfoCallBackEx", "cdecl")
    PlayM4_SetRunTimeInfoCallBackEx.argtypes = [LONG, c_int, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(RunTimeInfo), POINTER(None)), POINTER(None)]
    PlayM4_SetRunTimeInfoCallBackEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 850
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetRunTimeInfoCallbackType", "cdecl"):
    PlayM4_SetRunTimeInfoCallbackType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetRunTimeInfoCallbackType", "cdecl")
    PlayM4_SetRunTimeInfoCallbackType.argtypes = [c_int, c_int, c_uint, c_int]
    PlayM4_SetRunTimeInfoCallbackType.restype = c_int

enum_tagPLAYM4SRTextureMode = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 859

PLAYM4_TEXTURE_DOUBLE = 0x0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 859

PLAYM4_TEXTURE_OUTER = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 859

PLAYM4_TEXTURE_INNER = 0x2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 859

PLAYM4SRTEXTUREMODE = enum_tagPLAYM4SRTextureMode# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 859

enum_tagPLAYM4SRModelType = c_int# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 865

PLAYM4_MODELTYPE_HEMISPHERE = 0x0# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 865

PLAYM4_MODELTYPE_EAGLE_EYE = 0x1# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 865

PLAYM4_MODELTYPE_CUBE = 0x2# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 865

PLAYM4SRMODELTYPE = enum_tagPLAYM4SRModelType# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 865

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 880
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SR_SetConfig", "cdecl"):
    PlayM4_SR_SetConfig = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SR_SetConfig", "cdecl")
    PlayM4_SR_SetConfig.argtypes = [LONG, c_int, POINTER(None)]
    PlayM4_SR_SetConfig.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 881
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SR_Rotate", "cdecl"):
    PlayM4_SR_Rotate = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SR_Rotate", "cdecl")
    PlayM4_SR_Rotate.argtypes = [LONG, POINTER(PLAYM4SRTRANSFERPARAM)]
    PlayM4_SR_Rotate.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 882
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SR_Capture", "cdecl"):
    PlayM4_SR_Capture = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SR_Capture", "cdecl")
    PlayM4_SR_Capture.argtypes = [LONG, c_uint, String]
    PlayM4_SR_Capture.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 895
class struct_anon_412(Structure):
    pass

struct_anon_412.__slots__ = [
    'nType',
    'nStamp',
    'nFrameNum',
    'nBufLen',
    'pBuf',
    'stSysTime',
]
struct_anon_412._fields_ = [
    ('nType', c_long),
    ('nStamp', c_long),
    ('nFrameNum', c_long),
    ('nBufLen', c_long),
    ('pBuf', String),
    ('stSysTime', PLAYM4_SYSTEM_TIME),
]

RECORD_DATA_INFO = struct_anon_412# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 895

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 896
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RigisterDrawFun", "cdecl"):
    PlayM4_RigisterDrawFun = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RigisterDrawFun", "cdecl")
    PlayM4_RigisterDrawFun.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, HDC, POINTER(None)), POINTER(None)]
    PlayM4_RigisterDrawFun.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 897
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecCallBack", "cdecl"):
    PlayM4_SetDecCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecCallBack", "cdecl")
    PlayM4_SetDecCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, String, c_long, POINTER(FRAME_INFO), POINTER(None), POINTER(None))]
    PlayM4_SetDecCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 898
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecCallBackEx", "cdecl"):
    PlayM4_SetDecCallBackEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecCallBackEx", "cdecl")
    PlayM4_SetDecCallBackEx.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, String, c_long, POINTER(FRAME_INFO), POINTER(None), POINTER(None)), String, c_long]
    PlayM4_SetDecCallBackEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 899
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetSycStartTime", "cdecl"):
    PlayM4_SetSycStartTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetSycStartTime", "cdecl")
    PlayM4_SetSycStartTime.argtypes = [LONG, POINTER(PLAYM4_SYSTEM_TIME)]
    PlayM4_SetSycStartTime.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 900
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SyncToAudio", "cdecl"):
    PlayM4_SyncToAudio = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SyncToAudio", "cdecl")
    PlayM4_SyncToAudio.argtypes = [LONG, BOOL]
    PlayM4_SyncToAudio.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 901
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDecodeEngine", "cdecl"):
    PlayM4_SetDecodeEngine = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDecodeEngine", "cdecl")
    PlayM4_SetDecodeEngine.argtypes = [LONG, DWORD]
    PlayM4_SetDecodeEngine.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 902
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetRunTimeInfoCallBack", "cdecl"):
    PlayM4_SetRunTimeInfoCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetRunTimeInfoCallBack", "cdecl")
    PlayM4_SetRunTimeInfoCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(RunTimeInfo), POINTER(None)), POINTER(None)]
    PlayM4_SetRunTimeInfoCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 903
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetPreRecordFlag", "cdecl"):
    PlayM4_SetPreRecordFlag = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetPreRecordFlag", "cdecl")
    PlayM4_SetPreRecordFlag.argtypes = [LONG, BOOL]
    PlayM4_SetPreRecordFlag.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 904
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetPreRecordCallBack", "cdecl"):
    PlayM4_SetPreRecordCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetPreRecordCallBack", "cdecl")
    PlayM4_SetPreRecordCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(RECORD_DATA_INFO), POINTER(None)), POINTER(None)]
    PlayM4_SetPreRecordCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 905
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_InitDDraw", "cdecl"):
    PlayM4_InitDDraw = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_InitDDraw", "cdecl")
    PlayM4_InitDDraw.argtypes = [HWND]
    PlayM4_InitDDraw.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 906
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_RealeseDDraw", "cdecl"):
    PlayM4_RealeseDDraw = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_RealeseDDraw", "cdecl")
    PlayM4_RealeseDDraw.argtypes = []
    PlayM4_RealeseDDraw.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 907
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetFileEndMsg", "cdecl"):
    PlayM4_SetFileEndMsg = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetFileEndMsg", "cdecl")
    PlayM4_SetFileEndMsg.argtypes = [LONG, HWND, UINT]
    PlayM4_SetFileEndMsg.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 908
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetCaps", "cdecl"):
    PlayM4_GetCaps = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetCaps", "cdecl")
    PlayM4_GetCaps.argtypes = []
    PlayM4_GetCaps.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 909
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetOverlayMode", "cdecl"):
    PlayM4_SetOverlayMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetOverlayMode", "cdecl")
    PlayM4_SetOverlayMode.argtypes = [LONG, BOOL, COLORREF]
    PlayM4_SetOverlayMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 910
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetOverlayMode", "cdecl"):
    PlayM4_GetOverlayMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetOverlayMode", "cdecl")
    PlayM4_GetOverlayMode.argtypes = [LONG]
    PlayM4_GetOverlayMode.restype = LONG

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 911
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetColorKey", "cdecl"):
    PlayM4_GetColorKey = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetColorKey", "cdecl")
    PlayM4_GetColorKey.argtypes = [LONG]
    PlayM4_GetColorKey.restype = COLORREF

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 912
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_InitDDrawDevice", "cdecl"):
    PlayM4_InitDDrawDevice = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_InitDDrawDevice", "cdecl")
    PlayM4_InitDDrawDevice.argtypes = []
    PlayM4_InitDDrawDevice.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 913
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_ReleaseDDrawDevice", "cdecl"):
    PlayM4_ReleaseDDrawDevice = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_ReleaseDDrawDevice", "cdecl")
    PlayM4_ReleaseDDrawDevice.argtypes = []
    PlayM4_ReleaseDDrawDevice.restype = None

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 914
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetDDrawDeviceTotalNums", "cdecl"):
    PlayM4_GetDDrawDeviceTotalNums = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetDDrawDeviceTotalNums", "cdecl")
    PlayM4_GetDDrawDeviceTotalNums.argtypes = []
    PlayM4_GetDDrawDeviceTotalNums.restype = DWORD

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 915
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDDrawDevice", "cdecl"):
    PlayM4_SetDDrawDevice = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDDrawDevice", "cdecl")
    PlayM4_SetDDrawDevice.argtypes = [LONG, DWORD]
    PlayM4_SetDDrawDevice.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 916
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetDDrawDeviceInfo", "cdecl"):
    PlayM4_GetDDrawDeviceInfo = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetDDrawDeviceInfo", "cdecl")
    PlayM4_GetDDrawDeviceInfo.argtypes = [DWORD, LPSTR, DWORD, LPSTR, DWORD, POINTER(HMONITOR)]
    PlayM4_GetDDrawDeviceInfo.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 917
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetCapsEx", "cdecl"):
    PlayM4_GetCapsEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetCapsEx", "cdecl")
    PlayM4_GetCapsEx.argtypes = [DWORD]
    PlayM4_GetCapsEx.restype = c_int

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 918
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDDrawDeviceEx", "cdecl"):
    PlayM4_SetDDrawDeviceEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDDrawDeviceEx", "cdecl")
    PlayM4_SetDDrawDeviceEx.argtypes = [LONG, DWORD, DWORD]
    PlayM4_SetDDrawDeviceEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 919
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_OpenStreamEx", "cdecl"):
    PlayM4_OpenStreamEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_OpenStreamEx", "cdecl")
    PlayM4_OpenStreamEx.argtypes = [LONG, PBYTE, DWORD, DWORD]
    PlayM4_OpenStreamEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 920
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_CloseStreamEx", "cdecl"):
    PlayM4_CloseStreamEx = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_CloseStreamEx", "cdecl")
    PlayM4_CloseStreamEx.argtypes = [LONG]
    PlayM4_CloseStreamEx.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 921
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_InputVideoData", "cdecl"):
    PlayM4_InputVideoData = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_InputVideoData", "cdecl")
    PlayM4_InputVideoData.argtypes = [LONG, PBYTE, DWORD]
    PlayM4_InputVideoData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 922
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_InputAudioData", "cdecl"):
    PlayM4_InputAudioData = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_InputAudioData", "cdecl")
    PlayM4_InputAudioData.argtypes = [LONG, PBYTE, DWORD]
    PlayM4_InputAudioData.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 923
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetTimerType", "cdecl"):
    PlayM4_SetTimerType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetTimerType", "cdecl")
    PlayM4_SetTimerType.argtypes = [LONG, DWORD, DWORD]
    PlayM4_SetTimerType.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 924
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetTimerType", "cdecl"):
    PlayM4_GetTimerType = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetTimerType", "cdecl")
    PlayM4_GetTimerType.argtypes = [LONG, POINTER(DWORD), POINTER(DWORD)]
    PlayM4_GetTimerType.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 925
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetVerifyCallBack", "cdecl"):
    PlayM4_SetVerifyCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetVerifyCallBack", "cdecl")
    PlayM4_SetVerifyCallBack.argtypes = [LONG, DWORD, DWORD, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(FRAME_POS), DWORD, DWORD), DWORD]
    PlayM4_SetVerifyCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 926
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetAudioCallBack", "cdecl"):
    PlayM4_SetAudioCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetAudioCallBack", "cdecl")
    PlayM4_SetAudioCallBack.argtypes = [LONG, CFUNCTYPE(UNCHECKED(None), c_long, String, c_long, c_long, c_long, c_long), c_long]
    PlayM4_SetAudioCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 927
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetEncChangeMsg", "cdecl"):
    PlayM4_SetEncChangeMsg = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetEncChangeMsg", "cdecl")
    PlayM4_SetEncChangeMsg.argtypes = [LONG, HWND, UINT]
    PlayM4_SetEncChangeMsg.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 928
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetOriginalFrameCallBack", "cdecl"):
    PlayM4_GetOriginalFrameCallBack = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetOriginalFrameCallBack", "cdecl")
    PlayM4_GetOriginalFrameCallBack.argtypes = [LONG, BOOL, BOOL, c_long, c_long, c_long, CFUNCTYPE(UNCHECKED(None), c_long, POINTER(FRAME_TYPE), c_long), c_long]
    PlayM4_GetOriginalFrameCallBack.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 929
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetFileSpecialAttr", "cdecl"):
    PlayM4_GetFileSpecialAttr = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetFileSpecialAttr", "cdecl")
    PlayM4_GetFileSpecialAttr.argtypes = [LONG, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD)]
    PlayM4_GetFileSpecialAttr.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 930
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetPlayMode", "cdecl"):
    PlayM4_SetPlayMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetPlayMode", "cdecl")
    PlayM4_SetPlayMode.argtypes = [LONG, BOOL]
    PlayM4_SetPlayMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 931
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetOverlayFlipMode", "cdecl"):
    PlayM4_SetOverlayFlipMode = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetOverlayFlipMode", "cdecl")
    PlayM4_SetOverlayFlipMode.argtypes = [LONG, BOOL]
    PlayM4_SetOverlayFlipMode.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 932
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetDeflash", "cdecl"):
    PlayM4_SetDeflash = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetDeflash", "cdecl")
    PlayM4_SetDeflash.argtypes = [LONG, BOOL]
    PlayM4_SetDeflash.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 933
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetPicQuality", "cdecl"):
    PlayM4_SetPicQuality = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetPicQuality", "cdecl")
    PlayM4_SetPicQuality.argtypes = [LONG, BOOL]
    PlayM4_SetPicQuality.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 934
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_GetPictureQuality", "cdecl"):
    PlayM4_GetPictureQuality = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_GetPictureQuality", "cdecl")
    PlayM4_GetPictureQuality.argtypes = [LONG, POINTER(BOOL)]
    PlayM4_GetPictureQuality.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 935
if _libs["lib/win/PlayCtrl.dll"].has("PlayM4_SetGlobalBaseTime", "cdecl"):
    PlayM4_SetGlobalBaseTime = _libs["lib/win/PlayCtrl.dll"].get("PlayM4_SetGlobalBaseTime", "cdecl")
    PlayM4_SetGlobalBaseTime.argtypes = [c_long, PLAYM4_SYSTEM_TIME]
    PlayM4_SetGlobalBaseTime.restype = BOOL

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 9
try:
    PLAYM4_MAX_SUPPORTS = 500
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 10
try:
    MIN_WAVE_COEF = (-100)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 11
try:
    MAX_WAVE_COEF = 100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 12
try:
    TIMER_1 = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 13
try:
    TIMER_2 = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 14
try:
    BUF_VIDEO_SRC = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 15
try:
    BUF_AUDIO_SRC = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 16
try:
    BUF_VIDEO_RENDER = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 17
try:
    BUF_AUDIO_RENDER = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 18
try:
    BUF_VIDEO_DECODED = 5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 19
try:
    BUF_AUDIO_DECODED = 6
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 20
try:
    BUF_VIDEO_SRC_EX = 7
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 21
try:
    PLAYM4_NOERROR = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 22
try:
    PLAYM4_PARA_OVER = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 23
try:
    PLAYM4_ORDER_ERROR = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 24
try:
    PLAYM4_TIMER_ERROR = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 25
try:
    PLAYM4_DEC_VIDEO_ERROR = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 26
try:
    PLAYM4_DEC_AUDIO_ERROR = 5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 27
try:
    PLAYM4_ALLOC_MEMORY_ERROR = 6
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 28
try:
    PLAYM4_OPEN_FILE_ERROR = 7
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 29
try:
    PLAYM4_CREATE_OBJ_ERROR = 8
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 30
try:
    PLAYM4_CREATE_DDRAW_ERROR = 9
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 31
try:
    PLAYM4_CREATE_OFFSCREEN_ERROR = 10
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 32
try:
    PLAYM4_BUF_OVER = 11
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 33
try:
    PLAYM4_CREATE_SOUND_ERROR = 12
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 34
try:
    PLAYM4_SET_VOLUME_ERROR = 13
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 35
try:
    PLAYM4_SUPPORT_FILE_ONLY = 14
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 36
try:
    PLAYM4_SUPPORT_STREAM_ONLY = 15
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 37
try:
    PLAYM4_SYS_NOT_SUPPORT = 16
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 38
try:
    PLAYM4_FILEHEADER_UNKNOWN = 17
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 39
try:
    PLAYM4_VERSION_INCORRECT = 18
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 40
try:
    PLAYM4_INIT_DECODER_ERROR = 19
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 41
try:
    PLAYM4_CHECK_FILE_ERROR = 20
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 42
try:
    PLAYM4_INIT_TIMER_ERROR = 21
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 43
try:
    PLAYM4_BLT_ERROR = 22
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 44
try:
    PLAYM4_UPDATE_ERROR = 23
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 45
try:
    PLAYM4_OPEN_FILE_ERROR_MULTI = 24
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 46
try:
    PLAYM4_OPEN_FILE_ERROR_VIDEO = 25
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 47
try:
    PLAYM4_JPEG_COMPRESS_ERROR = 26
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 48
try:
    PLAYM4_EXTRACT_NOT_SUPPORT = 27
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 49
try:
    PLAYM4_EXTRACT_DATA_ERROR = 28
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 50
try:
    PLAYM4_SECRET_KEY_ERROR = 29
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 51
try:
    PLAYM4_DECODE_KEYFRAME_ERROR = 30
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 52
try:
    PLAYM4_NEED_MORE_DATA = 31
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 53
try:
    PLAYM4_INVALID_PORT = 32
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 54
try:
    PLAYM4_NOT_FIND = 33
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 55
try:
    PLAYM4_NEED_LARGER_BUFFER = 34
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 56
try:
    PLAYM4_FAIL_UNKNOWN = 99
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 57
try:
    PLAYM4_FEC_ERR_ENABLEFAIL = 100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 58
try:
    PLAYM4_FEC_ERR_NOTENABLE = 101
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 59
try:
    PLAYM4_FEC_ERR_NOSUBPORT = 102
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 60
try:
    PLAYM4_FEC_ERR_PARAMNOTINIT = 103
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 61
try:
    PLAYM4_FEC_ERR_SUBPORTOVER = 104
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 62
try:
    PLAYM4_FEC_ERR_EFFECTNOTSUPPORT = 105
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 63
try:
    PLAYM4_FEC_ERR_INVALIDWND = 106
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 64
try:
    PLAYM4_FEC_ERR_PTZOVERFLOW = 107
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 65
try:
    PLAYM4_FEC_ERR_RADIUSINVALID = 108
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 66
try:
    PLAYM4_FEC_ERR_UPDATENOTSUPPORT = 109
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 67
try:
    PLAYM4_FEC_ERR_NOPLAYPORT = 110
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 68
try:
    PLAYM4_FEC_ERR_PARAMVALID = 111
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 69
try:
    PLAYM4_FEC_ERR_INVALIDPORT = 112
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 70
try:
    PLAYM4_FEC_ERR_PTZZOOMOVER = 113
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 71
try:
    PLAYM4_FEC_ERR_OVERMAXPORT = 114
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 72
try:
    PLAYM4_FEC_ERR_ENABLED = 115
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 73
try:
    PLAYM4_FEC_ERR_D3DACCENOTENABLE = 116
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 74
try:
    PLAYM4_FEC_ERR_PLACETYPE = 117
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 75
try:
    PLAYM4_FEC_ERR_CorrectType = 118
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 76
try:
    PLAYM4_FEC_ERR_NULLWND = 119
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 77
try:
    PLAYM4_FEC_ERR_PARA = 120
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 78
try:
    MAX_DISPLAY_WND = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 79
try:
    DISPLAY_NORMAL = 0x00000001
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 80
try:
    DISPLAY_QUARTER = 0x00000002
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 81
try:
    DISPLAY_YC_SCALE = 0x00000004
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 82
try:
    DISPLAY_NOTEARING = 0x00000008
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 83
try:
    MAX_DIS_FRAMES = 50
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 84
try:
    MIN_DIS_FRAMES = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 85
try:
    BY_FRAMENUM = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 86
try:
    BY_FRAMETIME = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 87
try:
    SOURCE_BUF_MAX = (1024 * 100000)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 88
try:
    SOURCE_BUF_MIN = (1024 * 50)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 89
try:
    STREAME_REALTIME = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 90
try:
    STREAME_FILE = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 91
try:
    T_AUDIO16 = 101
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 92
try:
    T_AUDIO8 = 100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 93
try:
    T_UYVY = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 94
try:
    T_YV12 = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 95
try:
    T_RGB32 = 7
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 96
try:
    SUPPORT_DDRAW = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 97
try:
    SUPPORT_BLT = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 98
try:
    SUPPORT_BLTFOURCC = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 99
try:
    SUPPORT_BLTSHRINKX = 8
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 100
try:
    SUPPORT_BLTSHRINKY = 16
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 101
try:
    SUPPORT_BLTSTRETCHX = 32
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 102
try:
    SUPPORT_BLTSTRETCHY = 64
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 103
try:
    SUPPORT_SSE = 128
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 104
try:
    SUPPORT_MMX = 256
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 105
try:
    FOURCC_HKMI = 0x484B4D49
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 106
try:
    SYSTEM_NULL = 0x0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 107
try:
    SYSTEM_HIK = 0x1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 108
try:
    SYSTEM_MPEG2_PS = 0x2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 109
try:
    SYSTEM_MPEG2_TS = 0x3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 110
try:
    SYSTEM_RTP = 0x4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 111
try:
    SYSTEM_RTMP = 0xD
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 112
try:
    SYSTEM_RTPHIK = 0x401
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 113
try:
    SYSTEM_RTP_JT = 0x104
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 114
try:
    SYSTEM_DAH = 0x8001
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 115
try:
    VIDEO_NULL = 0x0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 116
try:
    VIDEO_H264 = 0x1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 117
try:
    VIDEO_MPEG2 = 0x2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 118
try:
    VIDEO_MPEG4 = 0x3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 119
try:
    VIDEO_MJPEG = 0x4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 120
try:
    VIDEO_AVC265 = 0x5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 121
try:
    VIDEO_SVAC = 0x6
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 122
try:
    VIDEO_AVC264 = 0x0100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 123
try:
    AUDIO_NULL = 0x0000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 124
try:
    AUDIO_ADPCM = 0x1000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 125
try:
    AUDIO_MPEG = 0x2000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 126
try:
    AUDIO_AAC = 0X2001
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 127
try:
    AUDIO_RAW_DATA8 = 0x7000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 128
try:
    AUDIO_RAW_UDATA16 = 0x7001
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 129
try:
    AUDIO_RAW_DATA8 = 0x7000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 130
try:
    AUDIO_RAW_UDATA16 = 0x7001
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 131
try:
    AUDIO_G711_U = 0x7110
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 132
try:
    AUDIO_G711_A = 0x7111
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 133
try:
    AUDIO_G722_1 = 0x7221
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 134
try:
    AUDIO_G723_1 = 0x7231
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 135
try:
    AUDIO_G726_U = 0x7260
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 136
try:
    AUDIO_G726_A = 0x7261
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 137
try:
    AUDIO_G726_16 = 0x7262
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 138
try:
    AUDIO_G729 = 0x7290
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 139
try:
    AUDIO_AMR_NB = 0x3000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 140
try:
    SYNCDATA_VEH = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 141
try:
    SYNCDATA_IVS = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 142
try:
    MOTION_FLOW_NONE = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 143
try:
    MOTION_FLOW_CPU = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 144
try:
    MOTION_FLOW_GPU = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 145
try:
    ENCRYPT_AES_3R_VIDEO = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 146
try:
    ENCRYPT_AES_10R_VIDEO = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 147
try:
    ENCRYPT_AES_3R_AUDIO = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 148
try:
    ENCRYPT_AES_10R_AUDIO = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 149
try:
    R_ANGLE_0 = (-1)
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 150
try:
    R_ANGLE_L90 = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 151
try:
    R_ANGLE_R90 = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 152
try:
    R_ANGLE_180 = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 548
try:
    HXVA_RESOLUTION_NONE = 0x00
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 549
try:
    HXVA_RESOLUTION_200W = 0x01
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 550
try:
    HXVA_RESOLUTION_300W = 0x02
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 551
try:
    HXVA_RESOLUTION_500W = 0x03
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 552
try:
    HXVA_RESOLUTION_800W = 0x04
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 553
try:
    HXVA_RESOLUTION_1600W = 0x05
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 554
try:
    HXVA_RESOLUTION_6400W = 0x06
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 622
try:
    PLAYM4_PROTOCOL_RTSP = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 623
try:
    PLAYM4_SESSION_INFO_SDP = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 670
try:
    FEC_UPDATE_RADIUS = 0x1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 671
try:
    FEC_UPDATE_PTZZOOM = 0x2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 672
try:
    FEC_UPDATE_WIDESCANOFFSET = 0x4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 673
try:
    FEC_UPDATE_PTZPARAM = 0x8
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 674
try:
    FEC_UPDATT_PTZCOLOR = 0x10
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 675
try:
    FEC_UPDATE_PTZSELECT = 0x20
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 709
try:
    FEC_JPEG = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 710
try:
    FEC_BMP = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 711
try:
    FEC_DISPLAYSURFACE = 0x400
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 724
try:
    FEC_DISPLAYSPHERE = 0x402
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 811
try:
    SOFT_DECODE_ENGINE = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 812
try:
    HARD_DECODE_ENGINE = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 815
try:
    PLAYM4_SOURCE_MODULE = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 816
try:
    PLAYM4_DEMUX_MODULE = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 817
try:
    PLAYM4_DECODE_MODULE = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 818
try:
    PLAYM4_RENDER_MODULE = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 819
try:
    PLAYM4_RTINFO_HARDDECODE_ERROR = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 820
try:
    PLAYM4_RTINFO_SOFTDECODE_ERROR = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 821
try:
    PLAYM4_RTINFO_MEDIAHEADER_ERROR = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 822
try:
    PLAYM4_RTINFO_SWITCH_SOFT_DEC = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 823
try:
    PLAYM4_RTINFO_ALLOC_MEMORY_ERROR = 4
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 824
try:
    PLAYM4_RTINFO_ENCRYPT_ERROR = 5
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 825
try:
    PLAYM4_RTINFO_RENDER_OVER = 8
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 826
try:
    PLAYM4_RTINFO_ERR_PRESENT = 16
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 827
try:
    PLAYM4_RTINFO_IDMX_DATA_ERROR = 32
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 828
try:
    PLAYM4_RTINFO_DECODE_PARAM_ERROR = 64
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 829
try:
    PLAYM4_RTINFO_SOFTDECODE_DATA_ERROR = 128
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 830
try:
    PLAYM4_RTINFO_IDMX_PSH_PSM_ERROR = 0x100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 831
try:
    PLAYM4_RTINFO_IDMX_RTP_HEADER_ERROR = 0x200
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 832
try:
    PLAYM4_RTINFO_IDMX_RTP_HEADER_SEQ_ERROR = 0x400
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 833
try:
    PLAYM4_RTINFO_IDMX_REDUNDANT_ERROR = 0x800
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 834
try:
    PLAYM4_RTINFO_IDMX_MEDIA_CHANGE_ERROR = 0x1000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 835
try:
    PLAYM4_RTINFO_IDMX_DIFFERENT_FRAMERATE_ERROR = 0x2000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 836
try:
    PLAYM4_RTINFO_IDMX_DIFFERENT_RESOLUTION_ERROR = 0x4000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 837
try:
    PLAYM4_RTINFO_IDMX_DECORD_ERROR = 0x8000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 838
try:
    PLAYM4_RTINFO_IDMX_PRIVT_LEN_ERROR = 0x10000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 839
try:
    PLAYM4_RTINFO_SOFTDECODE_DATA_FLAKE_ERROR = 0x20000
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 853
try:
    CFG_DISPLAY_MODEL_MODE = 0x499
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 866
try:
    PLAYM4_MODEL_SOLID = 0x0001
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 867
try:
    PLAYM4_MODEL_FRAME = 0x0010
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 868
try:
    PLAYM4_MODEL_AXIS = 0x0100
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 877
try:
    SR_JPEG = 0
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 878
try:
    SR_BMP = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 883
try:
    PLAYM4_MEDIA_HEAD = 1
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 884
try:
    PLAYM4_VIDEO_DATA = 2
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 885
try:
    PLAYM4_AUDIO_DATA = 3
except:
    pass

# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 886
try:
    PLAYM4_PRIVT_DATA = 4
except:
    pass

SYNCDATA_INFO = struct_SYNCDATA_INFO# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 193

_VCA_RECT_F_ = struct__VCA_RECT_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 200

_VCA_TARGET_EX = struct__VCA_TARGET_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 229

_VCA_TARGET_LIST_EX = struct__VCA_TARGET_LIST_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 234

_INTEL_INFO_EX = struct__INTEL_INFO_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 240

_VCA_POINT_F_ = struct__VCA_POINT_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 245

_VCA_POLYGON_F_ = struct__VCA_POLYGON_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 250

_VCA_ROTATE_RECT_F_ = struct__VCA_ROTATE_RECT_F_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 258

_VCA_REGION_ = struct__VCA_REGION_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 270

_VCA_TARGET_LIST_V1_EX_ = struct__VCA_TARGET_LIST_V1_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 285

_VCA_RULE_EX = struct__VCA_RULE_EX# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 292

_VCA_RULE_LIST_V3_EX_ = struct__VCA_RULE_LIST_V3_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 298

_VCA_ALERT_EX_ = struct__VCA_ALERT_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 306

_VCA_ALERT_LIST_EX_ = struct__VCA_ALERT_LIST_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 311

_PRIVATE_INFO_ = struct__PRIVATE_INFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 320

_HIK_MEDIAINFO_ = struct__HIK_MEDIAINFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 336

PLAYM4_SYSTEM_TIME = struct_PLAYM4_SYSTEM_TIME# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 387

_tagHDECODESUPPORT_ = struct__tagHDECODESUPPORT_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 569

_tagRENDERSUPPORT_ = struct__tagRENDERSUPPORT_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 579

_tagENGINESUPPORT_ = struct__tagENGINESUPPORT_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 585

_tagENGINESUPPORT_EX_ = struct__tagENGINESUPPORT_EX_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 595

_tagD3D11_PIC_INFO_ = struct__tagD3D11_PIC_INFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 605

_PLAYM4_SESSION_INFO_ = struct__PLAYM4_SESSION_INFO_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 629

tagCycleParam = struct_tagCycleParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 664

tagPTZParam = struct_tagPTZParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 669

tagFECColor = struct_tagFECColor# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 682

tagFECRectF = struct_tagFECRectF# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 689

tagFECParam = struct_tagFECParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 702

tagPLAYM4SRTransformElement = struct_tagPLAYM4SRTransformElement# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 718

tagPLAYM4SRTransformParam = struct_tagPLAYM4SRTransformParam# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 723

_PLAYM4_VIE_DYNPARAM_ = struct__PLAYM4_VIE_DYNPARAM_# C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_PlaySDK.h: 784

# No inserted files

# No prefix-stripping

