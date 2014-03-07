/*
 * Copyright 2013 Google Inc.
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

// Author: slamm@google.com (Stephen Lamm)
//
// Replace link tags with the inline CSS that is resolved on initial load.
// Move the link tags to the bottom (usually CSS is placed in HEAD). Also,
// copy existing inline style blocks to the bottom to maintain the original
// rule order.
//
// TODO(slamm): Consider prioritizing the rules in inline style blocks too.
//
// This lessons the extern resources in the HEAD and allows the page to load
// sooner.
//

#ifndef NET_INSTAWEB_REWRITER_PUBLIC_CRITICAL_CSS_FILTER_H_
#define NET_INSTAWEB_REWRITER_PUBLIC_CRITICAL_CSS_FILTER_H_

#include <vector>

#include "net/instaweb/htmlparse/public/empty_html_filter.h"
#include "net/instaweb/rewriter/public/css_tag_scanner.h"
#include "net/instaweb/util/public/basictypes.h"
#include "net/instaweb/util/public/scoped_ptr.h"
#include "net/instaweb/util/public/string_util.h"

namespace net_instaweb {

class CriticalCssFinder;
class HtmlCharactersNode;
class HtmlElement;
class RewriteDriver;

class CriticalCssFilter : public EmptyHtmlFilter {
 public:
  explicit CriticalCssFilter(RewriteDriver* rewrite_driver,
                             CriticalCssFinder* finder);
  virtual ~CriticalCssFilter();

  // Overridden from EmptyHtmlFilter:
  virtual void StartDocument();
  virtual void EndDocument();
  virtual void StartElement(HtmlElement* element);
  virtual void Characters(HtmlCharactersNode* characters);
  virtual void EndElement(HtmlElement* element);
  virtual const char* Name() const { return "CriticalCss"; }

 private:
  // Returns the critical CSS rules for the |decoded_url| of a <link> tag.
  // If data is unavailable (e.g., not yet determined, or flushed from
  //     page property cache), the returned StringPiece .data() is NULL.
  // If no CSS is critical for |decoded_url|, the returned StringPiece is empty.
  StringPiece GetRules(StringPiece decoded_url) const;

  RewriteDriver* driver_;
  CssTagScanner css_tag_scanner_;
  CriticalCssFinder* finder_;

  // Stores a map of CSS link URLs to critical CSS.
  scoped_ptr<StringStringMap> critical_css_map_;

  class CssElement;
  class CssStyleElement;
  typedef std::vector<CssElement*> CssElementVector;
  CssElementVector css_elements_;
  CssStyleElement* current_style_element_;
  bool has_critical_css_match_;

  DISALLOW_COPY_AND_ASSIGN(CriticalCssFilter);
};

}  // namespace net_instaweb

#endif  // NET_INSTAWEB_REWRITER_PUBLIC_CRITICAL_CSS_FILTER_H_