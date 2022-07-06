//
// sqratNull: nullptr support
//

//
// Copyright (c) 2009 Brandon Jones
//
// This software is provided 'as-is', without any express or implied
// warranty. In no event will the authors be held liable for any damages
// arising from the use of this software.
//
// Permission is granted to anyone to use this software for any purpose,
// including commercial applications, and to alter it and redistribute it
// freely, subject to the following restrictions:
//
//  1. The origin of this software must not be misrepresented; you must not
//  claim that you wrote the original software. If you use this software
//  in a product, an acknowledgment in the product documentation would be
//  appreciated but is not required.
//
//  2. Altered source versions must be plainly marked as such, and must not be
//  misrepresented as being the original software.
//
//  3. This notice may not be removed or altered from any source
//  distribution.
//

#if !defined(_SCRAT_NULL_H_)
#define _SCRAT_NULL_H_

#include <cstddef> // std::nullptr_t
#include "sqratTypes.h"

namespace Sqrat {
    template<>
    struct Var<std::nullptr_t> {

        std::nullptr_t value; ///< The actual value of get operations

        /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        /// Attempts to get the value off the stack at idx as an nullptr
        ///
        /// \param vm  Target VM
        /// \param idx Index trying to be read
        ///
        /// \remarks
        /// This function MUST have its Error handled if it occurred.
        ///
        /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        Var(HSQUIRRELVM vm, SQInteger idx) {
#if !defined (SCRAT_NO_ERROR_CHECKING)
            SQObjectType value_type = sq_gettype(vm, idx);
            if (value_type != OT_NULL) {
                SQTHROW(vm, FormatTypeError(vm, idx, _SC("null")));
            }
#endif
            value = nullptr;
        }

        /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        /// Called by Sqrat::PushVar to put an nullptr on the stack
        ///
        /// \param vm    Target VM
        /// \param value Value to push on to the VM's stack
        ///
        /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        static void push(HSQUIRRELVM vm, const std::nullptr_t value) {
            sq_pushnull(vm);
        }
    };
}
#endif