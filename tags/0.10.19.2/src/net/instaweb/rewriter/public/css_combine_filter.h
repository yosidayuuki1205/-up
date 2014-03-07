/*
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

// Author: jmarantz@google.com (Joshua Marantz)

#ifndef NET_INSTAWEB_REWRITER_PUBLIC_CSS_COMBINE_FILTER_H_
#define NET_INSTAWEB_REWRITER_PUBLIC_CSS_COMBINE_FILTER_H_

#include "base/scoped_ptr.h"
#include "net/instaweb/http/public/url_async_fetcher.h"
#include "net/instaweb/rewriter/public/css_tag_scanner.h"
#include "net/instaweb/rewriter/public/resource_manager.h"
#include "net/instaweb/rewriter/public/rewrite_filter.h"
#include "net/instaweb/util/public/basictypes.h"
#include "net/instaweb/util/public/url_multipart_encoder.h"

namespace net_instaweb {

class HtmlElement;
class HtmlIEDirectiveNode;
class MessageHandler;
class RequestHeaders;
class ResponseHeaders;
class RewriteContext;
class RewriteDriver;
class Statistics;
class UrlSegmentEncoder;
class Writer;

class CssCombineFilter : public RewriteFilter {
 public:
  // TODO(jmarantz): This BOM marker should be in some more central place,
  // rather than specific to css_combine_filter or even css.
  static const char kUtf8Bom[];

  CssCombineFilter(RewriteDriver* rewrite_driver, const char* path_prefix);
  virtual ~CssCombineFilter();

  static void Initialize(Statistics* statistics);
  virtual void StartDocumentImpl();
  virtual void StartElementImpl(HtmlElement* element);
  virtual void EndElementImpl(HtmlElement* element) {}
  virtual void Flush();
  virtual void IEDirective(HtmlIEDirectiveNode* directive);
  virtual const char* Name() const { return "CssCombine"; }
  virtual bool Fetch(const OutputResourcePtr& resource,
                     Writer* writer,
                     const RequestHeaders& request_header,
                     ResponseHeaders* response_headers,
                     MessageHandler* message_handler,
                     UrlAsyncFetcher::Callback* callback);
  virtual const UrlSegmentEncoder* encoder() const {
    return &multipart_encoder_;
  }

  virtual bool HasAsyncFlow() const;
  virtual RewriteContext* MakeRewriteContext();

 private:
  class Context;
  class CssCombiner;

  CssCombiner* combiner();
  void NextCombination();
  Context* MakeContext();

  CssTagScanner css_tag_scanner_;
  scoped_ptr<Context> context_;
  UrlMultipartEncoder multipart_encoder_;

  DISALLOW_COPY_AND_ASSIGN(CssCombineFilter);
};

}  // namespace net_instaweb

#endif  // NET_INSTAWEB_REWRITER_PUBLIC_CSS_COMBINE_FILTER_H_