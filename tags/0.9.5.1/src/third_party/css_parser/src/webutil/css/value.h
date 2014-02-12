/**
 * Copyright 2010 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Copyright 2006 Google Inc. All Rights Reserved.
// Author: dpeng@google.com (Daniel Peng)

#ifndef WEBUTIL_CSS_VALUE_H__
#define WEBUTIL_CSS_VALUE_H__

#include <string>
#include <vector>

#include "base/macros.h"
#include "base/scoped_ptr.h"
#include "util/utf8/public/unicodetext.h"
#include "webutil/css/identifier.h"
#include "webutil/css/string.h"
#include "webutil/html/htmlcolor.h"

// resolving conflict on macro HZ defined elsewhere.
#ifdef HZ
const int HZ_temporary = HZ;
#undef HZ
const int HZ = HZ_temporary;
#endif

namespace Css {

class Values;

// A Value represents a value in CSS (maybe more generally, a
// lexical unit).  There are many different types of these, so you can
// think of a Value as a tagged union of various values.  The tag
// is set by the constructor and accessed with GetLexicalUnitType().
// The values are also set by the constructor and accessed with the
// various accessors.
class Value {
 public:
  enum ValueType { NUMBER, URI, COUNTER, FUNCTION, RECT,
                   COLOR, STRING, IDENT, UNKNOWN, DEFAULT };
  enum Unit { EM, EX, PX, CM, MM, IN, PT, PC,
              DEG, RAD, GRAD, MS, S, HZ, KHZ, PERCENT, OTHER, NO_UNIT,
              NUM_UNITS };

  // These constructors generate Values of various types.

  Value() : type_(DEFAULT), color_(0, 0, 0) { }

  // UNKNOWN or DEFAULT
  Value(ValueType ty);  // NOLINT

  // NUMBER with unit.  OTHER is not a valid unit here.  Use the next form:
  Value(float num, Unit unit);

  // NUMBER with unit; we convert unit to an enum for you.  If it's
  // not a known unit, we use the OTHER enum and save the text.
  Value(float num, const UnicodeText& unit);

  // Any of the string types (URI, STRING). For IDENT, use the next
  // constructor instead.
  Value(ValueType ty, const UnicodeText& str);

  // IDENT from an identifier.
  explicit Value(const Identifier& identifier);
  explicit Value(const Identifier::Ident ident);

  // Any of the special function types (COUNTER, RECT)
  // NOTE: The ownership of params will be taken.
  // params cannot be NULL, if no parameters are needed, pass an empty Values.
  explicit Value(ValueType ty, Values* params);

  // FUNCTION with name func
  // NOTE: The ownership of params will be taken.
  // params cannot be NULL, if no parameters are needed, pass an empty Values.
  explicit Value(const UnicodeText& func, Values* params);

  // COLOR.
  explicit Value(HtmlColor color);

  // copy constructor and assignment operator
  Value(const Value& other);
  Value& operator=(const Value& other);

  // equality.
  bool Equals(const Value& other) const;

  // Given the text of a CSS unit, UnitFromText returns the
  // corresponding enum.  If no such unit is found, UnitFromText
  // returns OTHER.  Since all CSS units are ASCII, we are happy with
  // ASCII, UTF8, Latin-1, etc.
  static Unit UnitFromText(const char* s, int len);
  // Given a unit, returns its string representation.  If u is
  // NO_UNIT, returns "".  If u is OTHER, we return "OTHER", but this
  // may not be what you want.
  static const char* TextFromUnit(Unit u);

  // Returns a string representation of the value.
  string ToString() const;

  // Accessors.  Modeled after
  // http://www.w3.org/Style/CSS/SAC/doc/org/w3c/css/sac/LexicalUnit.html

  ValueType GetLexicalUnitType() const;  // The type of value

  // Each of these accessors is only valid for certain types.  The
  // comment indicates for which types they are valid; we DCHECK this
  // precondition.
  string    GetDimensionUnitText() const;  // NUMBER: the unit as a string.
  Unit      GetDimension() const;          // NUMBER: the unit.
  int       GetIntegerValue() const;       // NUMBER: the integer value.
  float     GetFloatValue() const;         // NUMBER: the float value.
  const Values* GetParameters() const;     // FUNCTION: the function params
  const UnicodeText& GetFunctionName() const;  // FUNCTION: the function name.
  const UnicodeText& GetStringValue() const;   // URI, STRING: the string value
  UnicodeText GetIdentifierText() const;   // IDENT: the ident as a string.
  const Identifier& GetIdentifier() const;        // IDENT: identifier.
  const HtmlColor&   GetColorValue() const;    // COLOR: the color value

 private:
  ValueType type_;  // indicates the type of value.  Always valid.
  float num_;             // for NUMBER (integer values are stored as floats)
  Unit unit_;             // for NUMBER
  Identifier identifier_;   // for IDENT
  UnicodeText str_;    // for NUMBER (OTHER unit_), URI, STRING, FUNCTION
  scoped_ptr<Values> params_;  // FUNCTION, COUNTER and RECT params
  HtmlColor color_;           // COLOR

  // kDimensionUnitText stores the name of each unit (see TextFromUnit)
  static const char* const kDimensionUnitText[];
};

// Values is a vector of Value*, which we own and will delete
// upon destruction.  If you remove elements from Values, you are
// responsible for deleting them.
// Also, be careful --- there's no virtual destructor, so this must be
// deleted as a Values.
class Values : public std::vector<Value*> {
 public:
  Values() : std::vector<Value*>() { }
  ~Values();

  // We provide syntactic sugar for accessing elements.
  // values->get(i) looks better than (*values)[i])
  const Value* get(int i) const { return (*this)[i]; }

  string ToString() const;
 private:
  DISALLOW_COPY_AND_ASSIGN(Values);
};

}  // namespace

#endif  // WEBUTIL_CSS_VALUE_H__