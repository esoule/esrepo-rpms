/*
 * Copyright (C) 2013 Red Hat, Inc.  All rights reserved.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 *
 * Authors: Peter Hatina <phatina@redhat.com>
 */

#ifndef __CONFIG_H__
#define __CONFIG_H__

#  include <bits/wordsize.h>

#  if __WORDSIZE == 32
#    include "config-32.h"
#  elif __WORDSIZE == 64
#    include "config-64.h"
#  else
#    error "Not supported architecture"
#  endif

#endif // __CONFIG_H__
