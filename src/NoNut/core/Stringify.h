#ifndef NONUT_CORE_STRINGIFY_H
#define NONUT_CORE_STRINGIFY_H

#include "CommonHeader.h"
#define QUOTIFY(arg) #arg
#define STRINGIFY(arg) QUOTIFY(arg)

namespace nonut
{
	template <typename T>
	class Stringify
	{
	public:
		virtual ~Stringify() = default;

		[[nodiscard]] virtual String toString() const
		{
			return STRINGIFY(T);
		}
	};
}
#endif //NONUT_CORE_STRINGIFY_H
